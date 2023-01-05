#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#

from typing import List

# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        '''
        s : input string composed of numbers and letters
        perms : output mutable array of strings containing upper and lower case permutations

        Algorithm: Use a decision tree to search for binary branches of upper and lower case characters.
        For each character we take each permutation and alter the permutations to be composed of a number or split
        that specific permutation to be composed of an upper and lower case form of the original permutation.

        breadth = 2^r, where r is the number of alphabetic characters
        so if we have 3 alphabetic characters in "a1b2c3" then the
        breadth is 8. Depth = n + 1, where n is the number of characters
        in the original string. So in "a1b2c3", n = 6 and Depth = 7
        
        breadth = 2^r = 2^3 = 8 
        depth = n + 1 = 6 + 1 = 7

        time T(n) = O(2^n)
        space S(n) = O(n2^n)

        '''
        s = [char for char in s]
        perms = [""]
        n = len(s)
        i = 1
        for i in range(0, n):
            tmp = []
            lowerChar = s[i].lower()
            unicodeChar = ord(lowerChar)
            if ord('a') <= unicodeChar <= ord('z'):
                # if we have an alphabetic char lower or uppercase
                for perm in perms:
                    lowerBranch = perm + s[i].lower()
                    upperBranch = perm + s[i].upper()
                    tmp.append(lowerBranch)
                    tmp.append(upperBranch)
            else:
                for perm in perms:
                    numberBranch = perm + s[i]
                    tmp.append(numberBranch)
            perms = tmp
        return perms
        
# @lc code=end

