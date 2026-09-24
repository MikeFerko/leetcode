#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
# https://leetcode.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (59.58%)
# Likes:    15352
# Dislikes: 255
# Total Accepted:    2M
# Total Submissions: 3.3M
# Testcase Example:  '"abcde"\n"ace"'
#
# Given two strings text1 and text2, return the length of their longest common
# subsequence. If there is no common subsequence, return 0.
# 
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative
# order of the remaining characters.
# 
# 
# For example, "ace" is a subsequence of "abcde".
# 
# 
# A common subsequence of two strings is a subsequence that is common to both
# strings.
# 
# 
# Example 1:
# 
# 
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# 
# 
# Example 2:
# 
# 
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# 
# 
# Example 3:
# 
# 
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.
# 
# 
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Given two strings text1 and text2, return the length of their 
        longest common subsequence. If there is no common subsequence, return 0.

        A subsequence of a string is a new string generated from the 
        original string with some characters (can be none) deleted without 
        changing the relative order of the remaining characters.

            - For example, "ace" is a subsequence of "abcde".
        
        A common subsequence of two strings is a subsequence that is 
        common to both strings.

        Algorithm:
            Dynamic programming tracks the previous row while scanning both strings.

        Args:
            text1 (str): The first string.
            text2 (str): The second string.

        Returns:
            int: The length of the longest common subsequence.
        
        @complexity:
            Time: T(m, n) = O(m * n), where m and n are the lengths of text1 and text2 respectively.
            Space: O(min(m, n)), using a rolling 1D DP array.
        """
        # Keep the DP array proportional to the shorter string.
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)
        for char1 in text1:
            diagonal = 0
            for j, char2 in enumerate(text2, 1):
                previous = dp[j]
                # Store the previous value before updating dp[j]
                if char1 == char2:
                    dp[j] = diagonal + 1
                else:
                    # If the characters do not match, take the maximum 
                    # of the current cell and the previous cell in the row.
                    dp[j] = max(dp[j], dp[j - 1])
                diagonal = previous

        return dp[-1]
        
# @lc code=end

