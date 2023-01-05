#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

from typing import List

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''binomial coefficient is from combinatory mathematics
        where the n choost k is the number of distinct subsets of size k of a set of size n.

        formula: nCk = n! / k! (n - k)!  
        our example: 
        4C2 = 4! / 2! (4 - 2)!
        => 4C2 = (4 x 3 x 2 x 1) / (2 x 1) (2!) = 12 / 2
        => 4C2 = 6 total combinations.
        time T(n, k) = O(k n^k) 
        '''
        comb = []
        def dfs(i: int, curr_res: List[int], n: int, k: int) -> List[int]:
            if i > n + 1:
                return
            if len(curr_res) == k:
                comb.append(curr_res.copy())
                return
            for j in range(i, n + 1):
                curr_res.append(j)
                dfs(j + 1, curr_res, n, k)
                curr_res.pop()         
        dfs(1, [], n, k)
        return comb



        
# @lc code=end

