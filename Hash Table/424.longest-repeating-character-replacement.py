#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (59.56%)
# Likes:    13540
# Dislikes: 801
# Total Accepted:    1.8M
# Total Submissions: 2.9M
# Testcase Example:  '"ABAB"\n2'
#
# You are given a string s and an integer k. You can choose any character of
# the string and change it to any other uppercase English character. You can
# perform this operation at most k times.
# 
# Return the length of the longest substring containing the same letter you can
# get after performing the above operations.
# 
# 
# Example 1:
# 
# 
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# 
# 
# Example 2:
# 
# 
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length
# 
# 
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Given a string s and an integer k, return the length
        of the longest substring containing the same letter 
        you can get after performing at most k operations of 
        changing any character to any other uppercase English character.

        Args:
            s (str): The input string consisting of uppercase English letters.
            k (int): The maximum number of operations allowed.
        
        Returns:
            int: The length of the longest substring with the same letter after at most k operations.
        
        @complexity: Time: T(n) = O(n)
        @complexity: Space: S(n) = O(1)

        The algorithm uses a sliding window. ``left`` and ``right`` define the
        current substring, while ``frequencies`` stores how often each letter
        occurs in that window. ``most_common`` is the highest frequency seen
        for one letter. To make the whole window contain the same letter, all
        other characters must be replaced, so the required replacements are
        ``window length - most_common``. If that value exceeds ``k``, move
        ``left`` forward until the window is valid again. The largest valid
        window length is returned.
        """
        frequencies = [0] * 26 # array is a faster lookup than a dict for this problem since we know the input is only uppercase letters.
        left = 0
        most_common = 0
        longest = 0

        for right in range(len(s)):
            index = ord(s[right]) - ord('A')
            frequencies[index] += 1
            most_common = max(most_common, frequencies[index])

            while (right - left + 1) - most_common > k:
                frequencies[ord(s[left]) - ord('A')] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest
        
        
# @lc code=end

