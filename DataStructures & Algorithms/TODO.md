# Future implementation ideas

Reference implementations worth adding to this folder later, same style as
the existing files (docstring header with complexity, class-based, camelCase,
driver code demo at the bottom).

## High value — gates an upcoming study plan week

- **Binary Search Tree** (insert/search/delete/in-order traversal) — Week 4
  has 3 BST problems (98, 230, 235) with nothing to warm up on first.
- **Backtracking template** (generic choose/explore/unchoose skeleton) —
  Week 2's backtracking block (Subsets, Permutations, Combination Sum) is
  one shape wearing different costumes.
- **Sliding Window template** — Week 2's window problems (Longest Substring
  Without Repeating Characters, Longest Repeating Character Replacement,
  Minimum Window Substring).
- **DP: memoization vs. tabulation side-by-side** — Week 3's whole DP
  progression; "which one do I reach for" is the recurring confusion,
  not the individual problems.

## Medium value — common interview asks, no specific week

- **LRU Cache** — combines hashTable.py + linkedList.py (already here) into
  one of the most common design-round questions.
- **Monotonic Stack/Queue** as its own named primitive — Daily Temperatures
  is solved, but the pattern itself isn't a reusable reference yet.
- **Quickselect** — natural extension of quickSort.py's partition step;
  gives the O(n)-average alternative to the heap approach used for 215.
- **Dijkstra's Algorithm** — shortest path on a weighted graph, natural
  next step after bredthFirstSearch.py / topologicalSort.py.

## Low priority — real, but not worth the time

- Segment Tree / Fenwick Tree (Binary Indexed Tree) — advanced range
  queries, rarely comes up outside specialized roles.
- Bellman-Ford — only matters over Dijkstra when edge weights can be
  negative; narrow use case.
