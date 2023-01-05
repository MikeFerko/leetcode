#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

from typing import List

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        nums : input array of possible houses to rob
        maxRob : ouput value of maximum cash ammount we can rob from all non adjacent houses and not alert the police

        Algorithm: Use D to keep track of previously robbed maximum house subproblems. Shift rob1 to rob2, make rob2
        the maximum rob we previously calculated so we iteratively keep track of the maximum value path in our decision tree.

        time T(n) = O(n)
        space S(n) = O(1)
        '''
        rob1, rob2 = 0, 0
        n = len(nums)
        for i in range(0, n):
            maxRob = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = maxRob
        return maxRob
# @lc code=end

