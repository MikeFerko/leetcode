#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (68.90%)
# Likes:    19038
# Dislikes: 981
# Total Accepted:    3.8M
# Total Submissions: 5.5M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Given an integer array nums and an integer k, return the k^th largest element
# in the array.
# 
# Note that it is the k^th largest element in the sorted order, not the k^th
# distinct element.
# 
# Can you solve it without sorting?
# 
# 
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
# 
# 
# Constraints:
# 
# 
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
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

