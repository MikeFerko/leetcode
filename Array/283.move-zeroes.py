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
        Do not return anything, modify nums in-place instead.
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

