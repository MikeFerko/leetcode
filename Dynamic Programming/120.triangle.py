#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

from typing import List

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        triangle : input triangle array
        dp : dp array of integers keeping track of bottom up minimum path sums from bottom triangle row
        up to top triangle row. where dp[0] will be our output integer
        
        Algorithm: bottom up dp keep track of minimum sums between parent node and it's two children.

        time T(n, m) = O(n*m) -> iterate through columns and rows all the way through, need to check every node to be sure of our path sums.
        space S(n) = O(n) -> store the dp array 
        '''
        n = len(triangle)
        dp = [0] * (n + 1)
        revTriangle = triangle[::-1]
        for i in range(0, n):
            revRow = revTriangle[i]
            m = len(revRow)
            for j in range(0, m):
                dp[j] = revRow[j] + min(dp[j], dp[j + 1])
        return dp[0]        
# @lc code=end

