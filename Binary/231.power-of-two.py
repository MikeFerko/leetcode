#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

import math

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        n : input integer
        output : if n is a power of two or not
        
        Algorithm: take the logarithm base 2 of the number 
        and if the floor and ceiling of that are equal 
        then we have a power of two.
        
        time T(n) = O(1) -> same number of operations every time.
        space S(n) = O(1) -> only store constants every time.
        
        could speed up by not using the math package.'''
        if n <= 0:
            return False # base case can't take log of 0/- number or we get a domain error
        return math.floor(math.log2(n)) == math.ceil(math.log2(n)) # _floor == _ceil 
        
# @lc code=end

