#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        n : input unsigned 32 bit integer
        ans : output reversed unsigned 32 bit integer
        
        Algorithm: right shift n by i bit places in the number and logic AND the right shifted n with 1
        to confirm we have a logic 1 or logic 0 in each bit place. Left shift this resulting bits by 
        31 minus the iteration number by using i. Compute a logic or with that and we will have reversed the 0th bit in n.
        Compute this 31 more times and we will have reversed every bit in n.
        
        time T(n) = O(1) -> consistantly will take only 32 iterations to complete.
        space S(n) = O(1) -> only need to store variables between the 32 iterations in the call stack.
        '''
        ans = 0
        for i in range(0, 32):
            bit = (n >> i) & 1
            ans = ans | (bit << (31 - i))
        return ans
# @lc code=end

