#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (38.99%)
# Likes:    45738
# Dislikes: 2242
# Total Accepted:    10.3M
# Total Submissions: 25.8M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without duplicate
# characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and
# "cab" are also correct answers.
# 
# 
# Example 2:
# 
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 10^5
# s consists of English letters, digits, symbols and spaces.
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest
        substring without duplicate characters.

        Use a sliding window for the longest substring.
        Keep a set of characters in our sliding window.
        Keep a longest substring length var.
        When the window contains a charater in our window that
        has already been seen in our window. Remove the character
        from our window. Calc the max or longest substring in our window
        iterating once through the length of the input string.

        Args:
            nums (str): input string

        Returns:
            int: the length of the longest substring

        @complexity: Time: O(n)
        @complexity: Space: O(n) (worst case store entire string as char set)
        """
        char_set = set()
        l = 0 # left window pointer
        lls = 0 # length of longest substring

        for r in range(len(s)): # r is the right window pointer
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            lls = max(lls, r - l + 1)
        return lls

# @lc code=end
