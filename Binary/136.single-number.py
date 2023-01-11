#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

from typing import List

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        nums : mutable input array of integers
        ans : output integer that is the non-duplicate number in nums
        
        Algorithm: Use logic xor between every number in nums. When there is 
        2 of the same binary representation of the same number we will get a logic 0 to remove
        those numbers and a logic 1 when the binary reresentation of those numbers are unique.
        
        time T(n) = O(n) -> we are bound by the number of iterations through the array.
        space S(n) = O(1) -> We only store the xor results as a variable with small spatial representation in memory.
        '''
        ans = 0
        n = len(nums)
        for i in range(0, n):
            ans = nums[i] ^ ans # ^ is the logical xor 
        return ans

# @lc code=end

