#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

from typing import List

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        nums : Array of integers
        target : target value we are searching for
        l :  low  index pointer in the array
        h : high index pointer in the array
        mid : middle pointer in the array 
        '''
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

