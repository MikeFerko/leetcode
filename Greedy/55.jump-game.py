#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (40.84%)
# Likes:    22158
# Dislikes: 1509
# Total Accepted:    3.4M
# Total Submissions: 8.3M
# Testcase Example:  '[2,3,1,1,4]'
#
# You are given an integer array nums. You are initially positioned at the
# array's first index, and each element in the array represents your maximum
# jump length at that position.
# 
# Return true if you can reach the last index, or false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        You are given an integer array `nums`. You are initially positioned at the
        array's first index, and each element in the array represents your maximum
        jump length at that position.

        Return `true` if you can reach the last index, or `false` otherwise.

        Algorithm:
            1. Initialize a variable `max_reachable` to 0, which will keep track of the farthest index we can reach.
            2. Iterate through the array using an index `i`.
            3. For each index `i`, check if `i` is greater than `max_reachable`. If it is, return `false` because we cannot reach this index.
            4. Update `max_reachable` to be the maximum of its current value and `i + nums[i]`, which represents the farthest index we can reach from index `i`.
            5. If we finish the loop without returning `false`, return `true` because we can reach the last index.

        Args:
            nums (List[int]): The input array representing maximum jump lengths.

        Returns:
            bool: `true` if we can reach the last index, `false` otherwise.

        @complexity:
            - Time complexity: T(n) = O(n), where n is the length of the input array `nums`. We iterate through the array once.
            - Space complexity: S(n) = O(1), as we use a constant amount of extra space.    
        """
        max_reachable = 0
        for i in range(len(nums)):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + nums[i])
        return True
        
# @lc code=end

