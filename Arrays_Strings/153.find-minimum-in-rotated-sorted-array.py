#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
'''
use left pivot middle and right pointers

if nums[middle] >= nums[left]:
    search the right portion of the array
else:
    search left portion of the array


'''

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            # initialy we have two values at the left and right pointer of the array
            if nums[left] < nums[right]:
                # take minimum of the two values
                result = min(result, nums[left])
                break
            
            # define the middle pointer as the sum of the left and right divided by two
            middle = (left + right) // 2
            # now take the minimum of the three values left middle and right
            result = min(result, nums[middle])

            if nums[middle] >= nums[left]:
                # search the right portion of the array by moving the left pointer
                # to the middle plus one to the right of the middle pointer
                left = middle + 1
            else:
                # search the left portion of the array by moving the left pointer
                # to the middle minus one to the left of the middle pointer
                right = middle - 1
        # return the result of our binary search
        return result
        
# @lc code=end
