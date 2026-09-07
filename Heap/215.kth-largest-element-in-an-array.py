#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

"""
Example 1:
    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5

Example 2:
    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4

First, lets try using a heap
Time Complexity: T(n) = O(nlogk)
Space Complexity: S(n) = O(k)

Store firest k-elements of nums in heap
Iterate from index k up to end of nums array
    If value nn is greater than weakest heap element
        Replace the weakest element
return weakest k-element after all elements are compared for heapreplacement.
"""

# @lc code=start
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """

        """
        heap = nums[:k]
        heapq.heapify(heap)
        for n in nums[k:]:
            if n > heap[0]:
                heapq.heapreplace(heap, n)
        return heap[0]

# @lc code=end
