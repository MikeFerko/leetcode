'''
Flatten a JSON-like Object

Turn an arbitrarily nested structure of dicts and lists into a single flat
dict whose keys are dot-separated paths to each leaf value. List elements
use their index as the path segment.

    {"a": {"b": 1, "c": [10, {"d": 2}]}}
        -> {"a.b": 1, "a.c.0": 10, "a.c.1.d": 2}

Rules:
    - Empty dicts/lists below the root are kept as leaf values ({} / []) so
      flattening doesn't silently drop them. An empty root flattens to {}.
    - A scalar root flattens to {"": value} -- the empty path is the root.
    - Dict keys must be strings (as from json.loads); anything else raises
      NonStringKeyError instead of being half-supported via str().
    - Two different paths producing the same flat key (e.g. {"a.b": 1} and
      {"a": {"b": 2}}) raise KeyCollisionError instead of overwriting.
    - escape=True backslash-escapes the separator inside keys, so those
      paths stay distinct: "a\\.b" vs "a.b".

Everything is built on one traversal (iterLeaves) and one key builder
(joinPath), so the validator and the flattener can never disagree about
what keys a record produces.

Time Complexity: T(n) = O(n * d), where n is the number of nodes in the
structure and d is the max depth -- every node is visited once, and each
leaf's path tuple and joined key cost up to O(d).
Space Complexity: S(n) = O(d) for the recursion stack, plus the output
dict and the origin map used to report collisions.
Recursion depth is bounded by Python's recursion limit (~1000 levels);
self-referencing (cyclic) objects hit that limit and raise RecursionError.
'''

import hashlib
import json
from collections import Counter
from dataclasses import dataclass, field
from typing import Any, Dict, Iterator, List, Optional, Tuple

# one segment per level: str for dict keys, int for list indices
Path = Tuple[Any, ...]

MODES = ("flexible", "strict", "escape")


class KeyCollisionError(ValueError):
    def __init__(self, key: str, paths: List[Path]):
        super().__init__(f"key collision on {key!r} from paths {paths}")
        self.key = key
        self.paths = paths


class NonStringKeyError(TypeError):
    def __init__(self, key: Any, path: Path):
        super().__init__(f"non-string key {key!r} at path {path}")
        self.key = key
        self.path = path


def iterLeaves(obj: Any) -> Iterator[Tuple[Path, Any]]:
    # the only place the structure is walked; yields (raw path, leaf value)
    def walk(node: Any, path: Path) -> Iterator[Tuple[Path, Any]]:
        if isinstance(node, dict) and node:
            for key, child in node.items():
                if not isinstance(key, str):
                    raise NonStringKeyError(key, path)
                # each level gets its own tuple, so there's no shared
                # path to append to and pop from
                yield from walk(child, path + (key,))
        elif isinstance(node, list) and node:
            for i, child in enumerate(node):
                yield from walk(child, path + (i,))
        elif path or not isinstance(node, (dict, list)):
            # leaf: a scalar, or an empty dict/list below the root
            # (an empty root yields nothing, so it flattens to {})
            yield path, node

    return walk(obj, ())


def escapeKey(key: str, separator: str) -> str:
    # escape the escape character first, so a literal backslash in a key
    # can't masquerade as an escaped separator
    return key.replace("\\", "\\\\").replace(separator, "\\" + separator)


def joinPath(path: Path, separator: str, escape: bool = False) -> str:
    segments = [str(p) for p in path]
    if escape:
        # escapeKey always gets the same separator the join uses
        segments = [escapeKey(s, separator) for s in segments]
    return separator.join(segments)


def checkSeparator(separator: str, escape: bool) -> None:
    if not separator:
        # "" is in every string and joins segments with no boundary at all
        raise ValueError("separator must be non-empty")
    if escape and "\\" in separator:
        raise ValueError("separator can't contain a backslash when escaping")


def flattenJson(obj: Any, separator: str = ".", escape: bool = False) -> Dict[str, Any]:
    checkSeparator(separator, escape)
    result: Dict[str, Any] = {}
    # flat key -> the path that produced it, so a collision can name both sides
    origins: Dict[str, Path] = {}

    for path, value in iterLeaves(obj):
        key = joinPath(path, separator, escape)
        if key in result:
            raise KeyCollisionError(key, [origins[key], path])
        result[key] = value
        origins[key] = path

    return result


@dataclass
class KeyReport:
    # flat key -> every original path that produces it
    collisions: Dict[str, List[Path]] = field(default_factory=dict)
    # paths down to each dict key that contains the separator, deduplicated
    riskyKeys: List[Path] = field(default_factory=list)


def inspectKeys(obj: Any, separator: str = ".", escape: bool = False) -> KeyReport:
    # same traversal and same key builder as flattenJson, but reports every
    # problem instead of raising on the first one
    checkSeparator(separator, escape)
    seen: Dict[str, List[Path]] = {}
    risky: Dict[Path, None] = {}  # dict as an ordered set

    for path, _ in iterLeaves(obj):
        seen.setdefault(joinPath(path, separator, escape), []).append(path)
        for i, segment in enumerate(path):
            # list indices are ints, so this only ever fires on dict keys
            if isinstance(segment, str) and separator in segment:
                risky[path[:i + 1]] = None

    return KeyReport(
        collisions={key: paths for key, paths in seen.items() if len(paths) > 1},
        riskyKeys=list(risky),
    )


@dataclass
class ProcessResult:
    outcome: str                            # "clean" | "quarantined"
    reason: Optional[str] = None            # why it was quarantined
    output: Optional[Dict[str, Any]] = None
    report: Optional[KeyReport] = None


def processRecord(record: Any, policy: Dict[str, Any]) -> ProcessResult:
    separator = policy.get("separator", ".")
    mode = policy.get("mode", "flexible")
    if mode not in MODES:
        # a bad policy is a config bug, not bad data -- don't quarantine it
        raise ValueError(f"unknown mode {mode!r}, expected one of {MODES}")
    escape = mode == "escape"

    try:
        report = inspectKeys(record, separator, escape)
    except NonStringKeyError:
        return ProcessResult("quarantined", "non_string_key")

    if report.collisions:
        return ProcessResult("quarantined", "key_collision", report=report)
    if mode == "strict" and report.riskyKeys:
        return ProcessResult("quarantined", "risky_key", report=report)

    return ProcessResult("clean", output=flattenJson(record, separator, escape), report=report)


def schemaPath(path: Path) -> Path:
    # orders.0.x and orders.1.x are one schema location, not two problems
    return tuple("*" if isinstance(p, int) else p for p in path)


@dataclass
class BatchStats:
    total: int = 0
    quarantined: int = 0
    recordsWithRiskyKeys: int = 0
    # schema path -> how many times that risky key appeared across the batch
    riskyKeyCounts: Counter = field(default_factory=Counter)


def partitionRecords(records: List[Any], policy: Dict[str, Any]):
    clean, quarantined, stats = [], [], BatchStats()

    for i, record in enumerate(records):
        stats.total += 1
        result = processRecord(record, policy)
        report = result.report

        if report and report.riskyKeys:
            stats.recordsWithRiskyKeys += 1
            stats.riskyKeyCounts.update(schemaPath(p) for p in report.riskyKeys)

        if result.outcome == "clean":
            clean.append(result.output)
        else:
            stats.quarantined += 1
            quarantined.append({
                "index": i,
                "reason": result.reason,
                "collisions": report.collisions if report else {},
                "riskyKeys": report.riskyKeys if report else [],
                "record": record,  # original, unmodified, so it can be replayed
            })

    return clean, quarantined, stats


def canonicalHash(obj: Any) -> str:
    # json.dumps alone would turn {1: "x"} into {"1": "x"} and hash both the
    # same, or crash sorting mixed key types -- reject non-string keys first
    for _ in iterLeaves(obj):
        pass
    # no default=str: non-JSON values (sets, objects) raise instead of being
    # stringified into something that might collide
    blob = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def makeReceipt(record: Any, policy: Dict[str, Any]) -> Dict[str, Any]:
    # records with non-string keys can't be hashed, so they get no receipt;
    # their quarantine entry keeps the raw record as the evidence instead
    result = processRecord(record, policy)
    return {
        "rawHash": canonicalHash(record),
        "policyHash": canonicalHash(policy),
        "outcome": result.outcome,
        "reason": result.reason,
        # quarantined records have no output -- their outcome + reason is
        # what a replay has to match, not an empty-string hash
        "outputHash": canonicalHash(result.output) if result.output is not None else None,
    }


def replay(record: Any, policy: Dict[str, Any], receipt: Dict[str, Any]) -> bool:
    if canonicalHash(record) != receipt["rawHash"]:
        raise ValueError("record doesn't match the receipt's rawHash")
    if canonicalHash(policy) != receipt["policyHash"]:
        raise ValueError("policy doesn't match the receipt's policyHash")
    # same record + same policy must reproduce the same outcome, reason and output
    return makeReceipt(record, policy) == receipt


# Driver code
if __name__ == "__main__":
    data = {
        "user": {
            "id": 7,
            "name": "Ada",
            "tags": ["admin", "ops"],
            "address": {"city": "Denver", "zip": None},
        },
        "orders": [
            {"id": 1, "items": [{"sku": "A1", "qty": 2}]},
            {"id": 2, "items": []},
        ],
        "meta": {},
        "active": True,
    }

    print("== basic flatten ==")
    for path, value in flattenJson(data).items():
        print(f"{path} = {value!r}")

    print("\n== edge cases ==")
    print("empty root:  ", flattenJson({}), flattenJson([]))
    print("scalar root: ", flattenJson(5))

    colliding = {"a.b": 1, "a": {"b": 2}}
    try:
        flattenJson(colliding)
    except KeyCollisionError as e:
        print("collision:   ", e)
    print("escaped:     ", flattenJson(colliding, escape=True))
    print("other sep:   ", flattenJson({"a/b": 1, "a": {"b": 2}}, separator="/", escape=True))

    try:
        flattenJson({1: "x"})
    except NonStringKeyError as e:
        print("non-str key: ", e)

    print("\n== batch partition ==")
    batch = [
        {"id": 1, "user": {"name": "Ada"}},                               # clean
        {"id": 2, "hosts": [{"api.example.com": "up"}]},                  # risky key
        {"id": 3, "a.b": 1, "a": {"b": 2}},                               # collision
        {"id": 4, 99: "bad"},                                             # non-string key
    ]
    for mode in MODES:
        clean, quarantined, stats = partitionRecords(batch, {"mode": mode})
        print(f"{mode:>8}: clean={len(clean)} quarantined="
              f"{[(q['record']['id'], q['reason']) for q in quarantined]} "
              f"risky={dict(stats.riskyKeyCounts)}")

    print("\n== receipts and replay ==")
    policy = {"mode": "flexible", "separator": "."}
    for record in batch[:3]:
        receipt = makeReceipt(record, policy)
        print(f"id={record['id']} outcome={receipt['outcome']} reason={receipt['reason']} "
              f"reproduced={replay(record, policy, receipt)}")

    tampered = makeReceipt(batch[0], policy) | {"outputHash": "0" * 64}
    print("tampered receipt reproduced:", replay(batch[0], policy, tampered))
