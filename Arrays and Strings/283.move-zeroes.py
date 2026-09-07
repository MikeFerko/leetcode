#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

from typing import List

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Given an array nums, move all 0's to the end while maintaining the
        relative order of the non-zero elements, in-place. Uses a slow
        pointer l marking the next non-zero write position while a fast
        pointer scans the array.

        Args:
            nums (List[int]): array to modify in-place

        Returns:
            None: modifies nums in-place instead

        @complexity: Time: O(n)
        @complexity: Space: O(1)
        """
        n = len(nums)
        l = 0
        for r in range(0, n):
            vall = nums[l]
            valr = nums[r]
            if valr:
                nums[l] = valr
                nums[r] = vall
                l += 1
                r = l
        
# @lc code=end

