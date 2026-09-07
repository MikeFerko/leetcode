#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

from typing import List

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Given a sorted array of distinct integers and a target value,
        return the index if the target is found. If not, return the index
        where it would be if it were inserted in order, using binary search.

        Args:
            nums (List[int]): sorted array of distinct integers
            target (int): value to search for or insert

        Returns:
            int: index of target, or the index it would be inserted at

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
        if target > nums[mid]:
            return mid + 1
        else:
            return mid
# @lc code=end

