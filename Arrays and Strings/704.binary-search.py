#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

from typing import List

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Given a sorted array of integers and a target value, return the
        index of target using binary search, or -1 if it is not present.

        Args:
            nums (List[int]): sorted array of integers
            target (int): value to search for

        Returns:
            int: index of target, or -1 if not found

        @complexity: Time: O(logn)
        @complexity: Space: O(1)
        """
        l, h = 0, len(nums) - 1

        while l <= h:
            mid = (l + h) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                h = mid - 1
        return -1
# @lc code=end

