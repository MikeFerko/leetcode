#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

from typing import List
# two pointers approach

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums sorted in non-decreasing order, return
        an array of the squares of each number sorted in non-decreasing
        order. Uses two pointers from each end, comparing squares and
        filling the output array from the back since the largest square
        must come from one of the two ends.

        Args:
            nums (List[int]): sorted array of integers

        Returns:
            List[int]: sorted array of squared values

        @complexity: Time: O(n)
        @complexity: Space: O(n)
        """
        n = len(nums)
        output = [0] * n
        l, r = 0, n - 1
        j = n - 1
        while r >= l:
            vall = nums[l] ** 2
            valr = nums[r] ** 2
            if vall > valr:
                output[j] = vall
                l += 1
            else:
                output[j] = valr
                r -= 1
            j -= 1
        return output


            
# @lc code=end

