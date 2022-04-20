#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

'''
Brute Force: count the number of 1s in n. Or we could right shift 
and mod the firts bit every time we shift the next bit position to find
if the remainer is one we add a one else we add zero and the count doens't go up.

# input is always a 32 bit integer so T(n) = O(32) = O(1) & S(n) = O(32) = O(1)

# another method is to subtract 1 from n and logic and that result with n:
n = n & (n - 1)
every time we perform this operation we add a 1 to our result

this algorithmic cycle of operations using a logic and with it's decremented value and counting the
number of times we perform that operation will result in the count of 1 bits in our 32 bit 
binary integer input.

Resulting in T(n) = O(1) & S(n) = O(1)

'''

# @lc code=start
# class bruteForce:
#     def hammingWeight(self, n: int) -> int:
#         hammingWeight = 0 # total number of ones
#         while n > 0:
#             hammingWeight += n % 2
#             n = n >> 1 # right bit shift by 1
#         return hammingWeight

class Solution:
    def hammingWeight(self, n: int) -> int:
        hammingWeight = 0 # total number of ones in binary input
        while n > 0:
            n = n & (n - 1)
            hammingWeight += 1
        return hammingWeight

# @lc code=end

