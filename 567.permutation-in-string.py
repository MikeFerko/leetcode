#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (48.80%)
# Likes:    13268
# Dislikes: 530
# Total Accepted:    1.6M
# Total Submissions: 3.3M
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise.
# 
# In other words, return true if one of s1's permutations is the substring of
# s2.
# 
# 
# Example 1:
# 
# 
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# Example 2:
# 
# 
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Given two strings s1 and s2, return true if s2 contains 
        a permutation of s1, or false otherwise.

        Algorithm:
            1. Create two frequency arrays of size 26 (for each letter 
               in the alphabet) to count the occurrences of each character 
               in s1 and the current window of s2.
            2. Initialize two pointers, left and right, to represent the 
               current window in s2.
            3. Expand the right pointer to include characters in the window 
               until the window size is equal to the length of s1.
            4. If the frequency arrays match, return True.
            5. If the window size exceeds the length of s1, move the left 
               pointer forward to shrink the window and update the frequency array accordingly.
            
        Args:
            s1 (str): The first input string.
            s2 (str): The second input string.

        Returns:
            bool: True if s2 contains a permutation of s1, False otherwise.
        """
        # If s1 is longer than s2, it cannot be a substring of s2.
        if len(s1) > len(s2):
            return False

        # Frequency counts for the pattern s1 and the current sliding window in s2.
        freq1: list[int] = [0] * 26
        freq2: list[int] = [0] * 26

        # Build the frequency map for s1.
        for char in s1:
            freq1[ord(char) - ord("a")] += 1

        window_size = len(s1)

        # Slide a window across s2 and compare its frequency map to s1's.
        for right, char in enumerate(s2):
            # Add the current character to the window.
            freq2[ord(char) - ord("a")] += 1

            # Once the window grows beyond the target length, remove the leftmost char.
            if right >= window_size:
                left_char = s2[right - window_size]
                freq2[ord(left_char) - ord("a")] -= 1

            # If the window frequency matches s1's frequency, a permutation exists.
            if freq1 == freq2:
                return True

        return False

        
# @lc code=end

