#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (31.79%)
# Likes:    13544
# Dislikes: 2422
# Total Accepted:    1.5M
# Total Submissions: 4.7M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string s and a pattern p, implement regular expression
# matching with support for '.' and '*' where:
# 
# 
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# 
# 
# Return a boolean indicating whether the matching covers the entire input
# string (not partial).
# 
# 
# Example 1:
# 
# 
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
# 
# 
# Example 3:
# 
# 
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a
# previous valid character to match.
# 
# 
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Given an input string s and a pattern p, implement regular expression
        matching with support for '.' and '*' where:
        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.

        Return a boolean indicating whether the matching covers the entire input
        string (not partial).

        Algorithm:
            Use dynamic programming to solve the problem.
            Create a 2D DP table where dp[i][j] represents whether s[:i] matches p[:j].
            Initialize dp[0][0] as True since empty string matches empty pattern.
            Fill the table based on the following rules:
            1. If p[j-1] is a letter or '.', check if s[i-1] matches p[j-1] and dp[i-1][j-1] is True.
            2. If p[j-1] is '*', check two cases:
               a. Treat '*' as zero occurrence of the preceding element: dp[i][j] = dp[i][j-2]
               b. Treat '*' as one or more occurrence if s[i-1] matches p[j-2]: dp[i][j] |= dp[i-1][j]
        
        Args:
            s (str): The input string.
            p (str): The pattern string containing letters, '.' and '*'.

        Returns:
            bool: True if the input string matches the pattern, False otherwise.
        
        @complexity:
            Time: T(s, p) = O(len(s) * len(p))
            Space: S(s, p) = O(len(s) * len(p))
        """
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] |= dp[i - 1][j]

        return dp[m][n]
        
# @lc code=end

