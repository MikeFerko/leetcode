#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        Given a sorted array of distinct integers and a target value, 
        return the index if the target is found. If not, 
        return the index where it would be if it were inserted in order.

        nums : array of integers to search
        target : integer value to search for
        l : low pointer
        h : high pointer
        mid : middle pointer
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
        if target > nums[mid]:
            return mid + 1
        else:
            return mid
# @lc code=end

