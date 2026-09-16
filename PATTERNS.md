# Patterns

A lookup table of the ~15 recurring patterns behind most LeetCode problems, built from
problems already solved in this repo. The goal isn't to memorize problems — it's to
recognize the *signal* in a new problem that points to one of these patterns. See the
solving framework below the table for the step-by-step process.

## Two Pointers
Signal: sorted array, or need to compare/consume from both ends without extra space.
- [Two Sum II - Input Array Is Sorted](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/167.two-sum-ii-input-array-is-sorted.py)
- [3 Sum](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/15.3-sum.py)
- [Container With Most Water](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/11.container-with-most-water.py)
- [Move Zeroes](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/283.move-zeroes.py)
- [Reverse String](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/344.reverse-string.py)
- [Reverse Words in a String III](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/557.reverse-words-in-a-string-iii.py)
- [Squares of a Sorted Array](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/977.squares-of-a-sorted-array.py)
- [Best Time to Buy and Sell Stock](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/bestTimeToBuyAndSellStock.py) (single-pass, low/high pointer)

## Sliding Window
Signal: "contiguous subarray/substring", "longest/shortest window satisfying X".
- [Longest Substring Without Repeating Characters](https://github.com/MikeFerko/leetcode/blob/master/Hash%20Table/3.longest-substring-without-repeating-characters.py)
- [Longest Repeating Character Replacement](https://github.com/MikeFerko/leetcode/blob/master/Hash%20Table/424.longest-repeating-character-replacement.py)
- [Permutation in String](https://github.com/MikeFerko/leetcode/blob/master/Hash%20Table/567.permutation-in-string.py) (fixed-size window)

## Binary Search
Signal: sorted (or "rotated sorted") array, or an answer space that's monotonic
("first true", "smallest value that satisfies X").
- [Binary Search](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/704.binary-search.py)
- [Search Insert Position](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/35.search-insert-position.py)
- [Find First and Last Position of Element in Sorted Array](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/34.find-first-and-last-position-of-element-in-sorted-array.py)
- [Search in Rotated Sorted Array](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/33.search-in-rotated-sorted-array.py)
- [Find Minimum in Rotated Sorted Array](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/153.find-minimum-in-rotated-sorted-array.py)
- [Find Peak Element](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/162.find-peak-element.py)
- [First Bad Version](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/278.first-bad-version.py) (answer-space binary search)
- [Search a 2D Matrix](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/74.search-a-2-d-matrix.py) (2D treated as flattened 1D)

## Prefix Sum
Signal: repeated range-sum queries, or "cumulative" totals.
- [Find the Highest Altitude](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/1732.find-the-highest-altitude.py)
- [Product of Array Except Self](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/productOfArrayExceptSelf.py) (prefix * suffix)

## Hash Map / Set
Signal: need O(1) lookup for "have I seen this", "does the complement exist", or
counting/grouping.
- [Two Sum](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/twoSum.py)
- [Contains Duplicate](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/containsDuplicate.py)

## Intervals (Sort + Sweep)
Signal: "merge/overlap/schedule/insert" over `[start, end]` ranges.
- [Merge Intervals](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/56.merge-intervals.py)
- [Insert Interval](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/57.insert-interval.py)
- [Non-overlapping Intervals](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/435.non-overlapping-intervals.py)

## Backtracking
Signal: "all subsets/permutations/combinations", "valid arrangements", build-check-undo.
- [Permutations](https://github.com/MikeFerko/leetcode/blob/master/DFS/46.permutations.py)
- [Combinations](https://github.com/MikeFerko/leetcode/blob/master/DFS/77.combinations.py)
- [Letter Case Permutation](https://github.com/MikeFerko/leetcode/blob/master/Tree/784.letter-case-permutation.py)

## BFS (Grid / Multi-source / Shortest Path)
Signal: "shortest path", "levels", "spread from multiple starting points simultaneously".
- [01 Matrix](https://github.com/MikeFerko/leetcode/blob/master/DFS/542.01-matrix.py) (multi-source BFS)
- [Rotting Oranges](https://github.com/MikeFerko/leetcode/blob/master/DFS/994.rotting-oranges.py) (multi-source BFS)
- [Binary Tree Level Order Traversal](https://github.com/MikeFerko/leetcode/blob/master/Tree/102.binary-tree-level-order-traversal.py)
- [Populating Next Right Pointers in Each Node](https://github.com/MikeFerko/leetcode/blob/master/Tree/116.populating-next-right-pointers-in-each-node.py)

## DFS (Traversal / Exploration)
Signal: explore all reachable cells/nodes from a start point, no need for shortest path.
- [Max Area of Island](https://github.com/MikeFerko/leetcode/blob/master/DFS/695.max-area-of-island.py)
- [Flood Fill](https://github.com/MikeFerko/leetcode/blob/master/DFS/733.flood-fill.py)
- [Merge Two Binary Trees](https://github.com/MikeFerko/leetcode/blob/master/Tree/617.merge-two-binary-trees.py)

## Dynamic Programming
Signal: "count the ways", "min/max cost/length", choice at each step with overlapping
subproblems and optimal substructure.
- [Climbing Stairs](https://github.com/MikeFerko/leetcode/blob/master/Dynamic%20Programming/70.climbing-stairs.py) (1D, Fibonacci-shaped)
- [House Robber](https://github.com/MikeFerko/leetcode/blob/master/Dynamic%20Programming/198.house-robber.py) (1D, take/skip)
- [Maximum Subarray](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/maximumSubarray.py) (Kadane's algorithm)
- [Maximum Product Subarray](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/maximumProductSubarray.py) (Kadane variant, track min & max)
- [Triangle](https://github.com/MikeFerko/leetcode/blob/master/Dynamic%20Programming/120.triangle.py) (bottom-up, 2D collapsed to 1D)
- [Longest Common Subsequence](https://github.com/MikeFerko/leetcode/blob/master/Dynamic%20Programming/1143.longest-common-subsequence.py) (2D grid DP)

## Monotonic Stack
Signal: "next greater/smaller element", need to look back and discard dominated values.
- [Daily Temperatures](https://github.com/MikeFerko/leetcode/blob/master/Stack/739.daily-temperatures.py)

## Stack (General)
Signal: matching/nesting, or need last-in-first-out undo/backtrack behavior.
- [Valid Parentheses](https://github.com/MikeFerko/leetcode/blob/master/Stack/20.valid-parentheses.py)
- [Min Stack](https://github.com/MikeFerko/leetcode/blob/master/Stack/155.min-stack.py) (auxiliary stack tracking running min)

## Fast & Slow Pointers (Linked List)
Signal: linked list, "cycle", "middle", "kth from the end", without extra space.
- [Middle of the Linked List](https://github.com/MikeFerko/leetcode/blob/master/Linked%20List/876.middle-of-the-linked-list.py)
- [Remove Nth Node From End Of List](https://github.com/MikeFerko/leetcode/blob/master/Linked%20List/19.remove-nth-node-from-end-of-list.py)

## Linked List Manipulation
Signal: rewiring `.next` pointers directly (reversal, merge, node deletion by value copy).
- [Reverse a Linked List](https://github.com/MikeFerko/leetcode/blob/master/Linked%20List/206.reverse-linked-list.py)
- [Merge Two Sorted Lists](https://github.com/MikeFerko/leetcode/blob/master/Linked%20List/21.merge-two-sorted-lists.py)
- [Delete Node in a Linked List](https://github.com/MikeFerko/leetcode/blob/master/Linked%20List/237.delete-node-in-a-linked-list.py) (no access to head, copy-and-skip trick)

## Bit Manipulation
Signal: constant extra space required on integers, XOR/AND/OR tricks, powers of two.
- [Sum of Two Integers](https://github.com/MikeFerko/leetcode/blob/master/Binary/371.sum-of-two-integers.py)
- [Number of 1 Bits](https://github.com/MikeFerko/leetcode/blob/master/Binary/191.number-of-1-bits.py)
- [Reverse Bits](https://github.com/MikeFerko/leetcode/blob/master/Binary/190.reverse-bits.py)
- [Single Number](https://github.com/MikeFerko/leetcode/blob/master/Binary/136.single-number.py) (XOR cancels pairs)
- [Power of Two](https://github.com/MikeFerko/leetcode/blob/master/Binary/231.power-of-two.py) (`n & (n-1) == 0`)

## Heap / Top-K
Signal: "k-th largest/smallest", "top k", "most/least frequent", need running min/max
under insertions.
- [Kth Largest Element in an Array](https://github.com/MikeFerko/leetcode/blob/master/Heap/215.kth-largest-element-in-an-array.py)
- [Top K Frequent Elements](https://github.com/MikeFerko/leetcode/blob/master/Heap/347.top-k-frequent-elements.py)
- [Task Scheduler](https://github.com/MikeFerko/leetcode/blob/master/Arrays%20and%20Strings/621.task-scheduler.py) (greedy + max-heap)

---

## Solving framework (run every new problem through this)

1. **Restate it.** Inputs, outputs, constraints, 2-3 examples including an edge case
   (empty, single element, duplicates, negatives). If you can't restate it, you don't
   understand it yet.
2. **Read the constraints — they dictate the required complexity.**

   | n | Required complexity | Implies |
   |---|---|---|
   | ≤ ~12 | O(2^n) / O(n!) | brute force / backtracking |
   | ≤ ~500 | O(n^3) | triple nested loop / simple DP |
   | ≤ ~5,000 | O(n^2) | nested loop, no shortcuts needed |
   | ≤ ~10^5-10^6 | O(n log n) or O(n) | sort+scan, heap, hashmap, two pointers, sliding window |
   | ≤ ~10^9 | O(log n) or O(1) | binary search, math |

3. **Match the surface signal to a pattern** using the table above.
4. **Write brute force first** (even mentally) — it gives you a correctness baseline and
   usually reveals the exact bottleneck (nested loop, recomputation) that the pattern
   exists to remove.
5. **State the invariant** your loop/pointer/window maintains in one sentence before
   coding it.
6. **After solving, tag it** with its pattern in this file — the determinism comes from
   repeating the *pattern*, not the problem.
