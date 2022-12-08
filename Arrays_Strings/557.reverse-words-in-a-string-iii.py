#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        s : input string
        l : left pointer of each word as we iterate left to right
        r : right pointer of each word as we iterate left to right
        r will tell us where the end of each word is

        algorithm: 
        1. iterate through the string and point to the start of each word
        and end of each word pass the start and end into a reversal to only reverse
        the word between the start and end of the string and retern that string
        with the one reversed word and assign it to the original string.
        2. Iterate start until the end of the string. Iterate end until the end of the string
        and when string[end] is not a space char.
        3. When the space char is found: start will point at the start of a word. End will
        point at the space after each word
        4. Reverse the string from the start of the word in the string until the end of the
        string - 1 because end points to the space after our word.
        5. return the original string with the reversed word in place.
        6. return the string with reversed order of chars in each word while having preserved
        the whitespace and initial word order

        time T(n) = O(n) -> iterate through the entire word
        space S(n) -> O(1) -> we store the array of each word with the chars split,
        it grows with the number of words in the original string, but we can say it is a constant in terms
        of not using any extra space when the reverse string method is called each time.

        '''
        start, end = 0, 0
        while start < len(s):
            while end < len(s) and s[end] != ' ':
                end += 1
            s = self.reverseString(s, start, end)
            start = end + 1 # when end is pointing at a space character
            end = start # reset end pointer to the start of another word
        return s

    def reverseString(self, s: str, start: int, end: int) -> str:
        '''
        s : input string
        start : start of reversal of the string
        end : end of the reversal of the string
        l : left pointer in word from string s
        r : right pointer in word from string s
        '''
        s = list(s)
        l, r = start, end - 1
        while l < r:
            vall = s[l]
            valr = s[r]
            s[l] = valr
            s[r] = vall
            l += 1
            r -= 1
        return ''.join(s)




# @lc code=end

