#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        s : input string
        llns : output length of longest non-repeating substring
        l : left pointer in sliding window
        r : right pointer in sliding window
        n : length of input string
        charSet : Hash set of characters window

        Aglortithm: initialize a window of length 0. Remove chars from the
        left of the sliding window charset until the right character is not in 
        the char set. add the right character when it is not in the char set.
        Get the length between the right and left pointer in the sliding window
        and take it as the maximum between the window and previous iterations.
        
        time T(n) = O(n) -> iterate through the length of the string once
        space S(n) = O(n) -> worst case store the entire length of the string
        '''
        charSet = set()
        l, r = 0, 0
        n = len(s)
        llns = 0

        while r <= n - 1:
            rc = s[r]
            while rc in charSet:
                lc = s[l]
                charSet.remove(lc)
                l += 1
            charSet.add(rc)
            llns = max(llns, r - l + 1)
            r += 1
        return llns
        
# @lc code=end

