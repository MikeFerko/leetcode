#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

from typing import List

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        nums : input mutable array of integers
        target : input integer to search for in nums to find the first and last occurance index
        left : left biased integer from our binary search
        right : right biased integer from our binary search

        Algorithm : Use a bias to search to the left or right of our binary search so we get the 
        first meaning the left or last occurance meaning the right from our binary search. This can
        be done using the usual mid/median shift that is already part of the binary search.

        time T(n) = O(lgn) -> lg = log base 2 -> we will search twice to get the first (left) and last occurance (right)
        space S(n) = O(1) -> store only constants i.e. no complex data structure to store a lot of extra information
        '''
        left = self.binarySearch(nums, target, leftBiased=True)
        right = self.binarySearch(nums, target, leftBiased=False)
        return [left, right]
    
    def binarySearch(self, nums: List[int], target: int, leftBiased: bool) -> int:
        n = len(nums)
        l, r = 0, n - 1
        i = -1
        while l <= r:
            mid = abs(r + l) // 2 # floored
            if target == nums[mid]:
                i = mid
                if leftBiased:
                    r = mid - 1
                else:
                    l = mid + 1
            if target > nums[mid]:
                l = mid + 1
            if target < nums[mid]:
                r = mid - 1 
        return i
            
        
# @lc code=end

