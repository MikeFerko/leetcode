#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Given an integer array nums and an integer k, return the kth largest
        element in the array. Store the first k elements in a min-heap, then
        for each remaining element replace the heap's minimum whenever a
        larger value is found. The heap's root is the kth largest element
        once all elements have been considered.

        Args:
            nums (List[int]): array of integers
            k (int): the rank (from largest) of the element to find

        Returns:
            int: the kth largest element in nums

        @complexity: Time: O(nlogk)
        @complexity: Space: O(k)
        """
        heap = nums[:k]
        heapq.heapify(heap)
        for n in nums[k:]:
            if n > heap[0]:
                heapq.heapreplace(heap, n)
        return heap[0]

# @lc code=end