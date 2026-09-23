#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (59.99%)
# Likes:    23066
# Dislikes: 522
# Total Accepted:    2.8M
# Total Submissions: 4.7M
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an integer array nums, return the length of the longest strictly
# increasing subsequence.
# 
# 
# Example 1:
# 
# 
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1,0,3,2,3]
# Output: 4
# 
# 
# Example 3:
# 
# 
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
# 
# 
# 
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
# complexity?
# 
#

# @lc code=start
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Given an integer array nums, return the length of the longest strictly
        increasing subsequence.
        
        Algorithm:
            Maintain `dp`, where `dp[i]` is the smallest possible tail of an
            increasing subsequence of length `i + 1`. Use binary search to find
            the first tail greater than or equal to each number and replace it.

        Args:
            nums (List[int]): The list of integers.

        Returns:
            int: The length of the longest strictly increasing subsequence.

        @complexity:
            Time: T(n) = O(n log n); where n is the length of the input list.
            Space: S(n) = O(n); where n is the length of the input list.
        """
        dp = [] # dp[i] will hold the smallest tail of all increasing subsequences of length i+1
        for num in nums:
            # Find the first element in dp which is greater than or equal to num.
            left, right = 0, len(dp)
            # Binary search to find the position to replace or append the current number.
            while left < right:
                middle = (left + right) // 2
                if dp[middle] < num:
                    left = middle + 1
                else:
                    right = middle
            # Determine the index where the current number should be placed in dp.
            index = left
            if index == len(dp):
                dp.append(num)
            else:
                dp[index] = num
        return len(dp)
# @lc code=end

