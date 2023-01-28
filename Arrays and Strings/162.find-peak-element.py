#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

from typing import List

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        input: mutable array of integers
        output: integer index of local maxima/a peak element

        Algorithm: binary search array to find a single maxima that is larger than the element 
        before and after it in the array. Doesn't matter if it's the global or local.

        time T(n) = O(lg n) -> binary log is lg
        space S(n) = O(1) -> store no more than constants between instantiations of the method.
        '''
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l

# @lc code=end

