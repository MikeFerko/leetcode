#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (68.25%)
# Likes:    37213
# Dislikes: 729
# Total Accepted:    3.9M
# Total Submissions: 5.7M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
# 
# 
# Example 1:
# 
# 
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
# 
# 
# Example 2:
# 
# 
# Input: height = [4,2,0,3,2,5]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Given n non-negative integers representing an 
        elevation map where the width of each bar is 1, 
        compute how much water it can trap after raining.

        Algorithm:
            1. Initialize two pointers, left and right, at the start and end of the height array.
            2. Initialize two variables, left_max and right_max, to keep track of the maximum height encountered from the left and right.
            3. Initialize a variable, water_trapped, to 0.
            4. While left is less than right:
                a. If height[left] is less than height[right]:
                    i. If height[left] is greater than left_max, update left_max.
                    ii. Else, add left_max - height[left] to water_trapped.
                    iii. Move left pointer to the right.
                b. Else:
                    i. If height[right] is greater than right_max, update right_max.
                    ii. Else, add right_max - height[right] to water_trapped.
                    iii. Move right pointer to the left.
            5. Return water_trapped.
        
        Args:
            height (List[int]): A list of non-negative integers representing the elevation map.

        Returns:
            int: The total amount of water that can be trapped after raining.
        
        @complexity:
            Time: T(n) = O(n)
            Space: S(n) = O(1)
        
        """
        left, right = 0, len(height) - 1
        left_max = right_max = water_trapped = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    water_trapped += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water_trapped += right_max - height[right]
                right -= 1
        
        return water_trapped

# @lc code=end

