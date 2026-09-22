#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (45.57%)
# Likes:    11327
# Dislikes: 200
# Total Accepted:    1.4M
# Total Submissions: 3M
# Testcase Example:  '[2,3,2]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have a security system connected, and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
# 
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the
# police.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money =
# 2), because they are adjacent houses.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        You are a professional robber planning to rob houses along a street. Each
        house has a certain amount of money stashed. All houses at this place are
        arranged in a circle. That means the first house is the neighbor of the last
        one. Meanwhile, adjacent houses have a security system connected, and it will
        automatically contact the police if two adjacent houses were broken into on
        the same night.

        Given an integer array nums representing the amount of money of each house,
        return the maximum amount of money you can rob tonight without alerting the
        police.

        Algorithm:
            1. If there is only one house, return the amount in that house.
            2. If there are two houses, return the maximum of the two amounts.
            3. For more than two houses, calculate the maximum amount that can be
            robbed by considering two scenarios:
                a. Robbing from the first house to the second-to-last house (excluding
                the last house).
                b. Robbing from the second house to the last house (excluding the
                first house).
            4. Return the maximum of the two scenarios.
        
        Args:
            nums (List[int]): The list of amounts in each house.
        
        Returns:
            int: The maximum amount of money that can be robbed without alerting the
            police.
        
        @complexity:
            Time: T(n) = O(n), where n is the number of houses. We traverse the list twice.
            Space: S(n) = O(1), as we use a constant amount of space for variables.
        """
        n = len(nums)

        # edge cases for 1 or 2 houses.
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # Helper function to calculate the maximum amount that can be robbed in a linear arrangement of houses.
        # from 198.house-robber.py
        def rob_linear(houses: List[int]) -> int:
            if not houses:
                return 0
            prev1, prev2 = 0, 0
            for amount in houses:
                current = max(prev1, prev2 + amount)
                prev2 = prev1
                prev1 = current
            return prev1

        # Scenario 1: Rob from the first house to the second-to-last house
        max_rob1 = rob_linear(nums[:-1])

        # Scenario 2: Rob from the second house to the last house
        max_rob2 = rob_linear(nums[1:])

        return max(max_rob1, max_rob2)
# @lc code=end

