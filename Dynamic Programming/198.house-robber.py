#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Medium (53.61%)
# Likes:    23918
# Dislikes: 527
# Total Accepted:    3.9M
# Total Submissions: 7.2M
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security systems
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
# 
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the
# police.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        You are a professional robber planning to rob houses along a street. Each
        house has a certain amount of money stashed, the only constraint stopping you
        from robbing each of them is that adjacent houses have security systems
        connected and it will automatically contact the police if two adjacent houses
        were broken into on the same night.

        Given an integer array nums representing the amount of money of each house,
        return the maximum amount of money you can rob tonight without alerting the
        police.

        Algorithm:
            1. Use dynamic programming to keep track of the maximum amount of money that
                can be robbed up to each house.
            2. For each house, decide whether to rob it or skip it based on the maximum amount
                that can be robbed from the previous houses.
            3. Return the maximum amount of money that can be robbed from all houses.            

        Args:
            nums (List[int]): The list of money in each house.

        Returns:
            int: The maximum amount of money you can rob tonight without alerting the police.
        
        @complexity:
            Time complexity: T(n) = O(n), where n is the number of houses. We iterate through the list of houses once.
            Space complexity: S(n) = O(1), we use a constant amount of space for variables to store the maximum amounts.
        """
        # edge case: if the list of houses is empty, return 0
        if not nums:
            return 0
        # Initialize two variables to keep track of the maximum amount of money that can be robbed up to the previous two houses
        prev1, prev2 = 0, 0
        for num in nums:
            # Calculate the maximum amount of money that can be robbed up to the current house
            current = max(prev1, prev2 + num)
            # Update the variables for the next iteration
            prev2 = prev1
            prev1 = current
        # Return the maximum amount of money that can be robbed from all houses
        return prev1

# @lc code=end

