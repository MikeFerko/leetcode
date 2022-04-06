#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

"""
Ex1: 
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

brute force: try every single combination with two pointers left
and right. Left ponter runs through the array n time and the right pointer
checks each value n times resulting in O(n**2) maximum area checks in time.
Time Complexity: T(n) = O(n**2)

Next, lets use a two pointer solution. Start with left pointer at start
of the array and right at n - 1
shift one or the other based on which pointer is smaller
Time Complexity: T(n) = O(n)
Space Complexity: S(n) = O(1)
"""
from typing import List

# @lc code=start

# quadratic time solution
class bruteForce: # this is too slow.
    def maxArea(self, height: List[int]) -> int:
        result = 0 # max area returned
        n = len(height)

        for left in range(0, n):
            for right in range(left + 1, n):
                area = (right - left) * min(height[left],height[right])
                result = max(result,area)
        return result

# linear time solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0 # max area returned
        n = len(height)
        left = 0
        right = n - 1

        while left < right:
            area = (right - left) * min(height[right],height[left])
            result = max(result,area)
            # shift right or left pointer based on which pointer is smaller
            if height[left] < height[right]:
                left += 1
            # elif height[right] > height[left]:
            #     right -= 1
            else:
                right -= 1
        return result
# @lc code=end

