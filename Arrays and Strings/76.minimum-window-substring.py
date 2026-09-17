#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (47.46%)
# Likes:    20687
# Dislikes: 867
# Total Accepted:    2.4M
# Total Submissions: 4.9M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates)
# is included in the window. If there is no such substring, return the empty
# string "".
# 
# The testcases will be generated such that the answer is unique.
# 
# 
# Example 1:
# 
# 
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
# from string t.
# 
# 
# Example 2:
# 
# 
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# 
# 
# Example 3:
# 
# 
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
# 
# 
# 
# Constraints:
# 
# 
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
# 
# 
# 
# Follow up: Could you find an algorithm that runs in O(m + n) time?
# 
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Given two strings s and t, find the minimum window
        in s which will contain all the characters in t in complexity O(n).

        Algorithm:
        Use a sliding window with two pointers. Expand the right pointer to include
        characters from t, then shrink the left pointer while the window still
        contains all required characters. Keep track of the smallest valid window.

        Args:
            s (str): The source string.
            t (str): The target string containing required characters.
        
        Returns:
            str: The minimum window substring of s that contains all characters of t.
        
        @complexity:
            Time: O(m + n), where m is the length of s and n is the length of t.
            Space: O(n), for storing character counts of t and the current window.
        """
        # Edge cases and an impossible-length shortcut.
        if not s or not t or len(t) > len(s):
            return ""

        # Fixed-size storage for ASCII characters keeps the auxiliary space O(1).
        # Positive values represent characters still required; negative values
        # represent extra occurrences currently covered by the window.
        need = [0] * 128
        for ch in t:
            need[ord(ch)] += 1

        # `missing` counts individual characters from t that are not yet covered.
        missing = len(t)
        left = 0
        best_start = 0
        best_len = len(s) + 1

        for right, ch in enumerate(s):
            index = ord(ch)
            # A character that was still needed makes the window more complete.
            if need[index] > 0:
                missing -= 1
            need[index] -= 1

            # Once valid, move the left edge rightward to remove unnecessary
            # characters and obtain the smallest valid window ending at `right`.
            while missing == 0:
                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_start = left

                left_index = ord(s[left])
                need[left_index] += 1
                # If removing this character makes it needed again, the window
                # is no longer valid and expansion must resume.
                if need[left_index] > 0:
                    missing += 1
                left += 1

        # `best_len` remains larger than s when no valid window was found.
        return "" if best_len > len(s) else s[best_start:best_start + best_len]

# @lc code=end
