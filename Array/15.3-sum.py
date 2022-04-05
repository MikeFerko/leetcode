#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
"""
Ex1: 
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

want three values that sum to zero:

nums[i] + nums[j] + nums[k] = 0

could brute force triple loop with conditionals

We could sort the array and then when we look for our combinations where
we can ignore neighbors that have the same values so as to skip redundant 
opperations.

Since our array is sorted we can use left and right pointers along the
rest of the array to see what shifted pointer locations add up to the
opposite sign of the first value so as to achieve a zero net sum.

i.e. state: sum > 0 -> action: shift right pointer to the left
    state: sum < 0 -> action: shift left pointer to the right

Time Complexity: T(n) = O(n lg n) + O(n**2) = O(n**2)
Space Complexity: S(n) = O(1) or O(n) depending on the sorting storage based on the library used.
"""

from typing import List

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        n = len(nums)
        for i in range(0, n):
            if i > 0 and nums[i] == nums[i - 1]:
                # if we have the same value as the previous we 
                # want to continue through the array and ignore that ith value
                continue
            left, right = i + 1, n - 1 
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1 
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1 
        return result
        
# @lc code=end
