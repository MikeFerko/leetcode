#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (49.17%)
# Likes:    21338
# Dislikes: 553
# Total Accepted:    3.1M
# Total Submissions: 6.3M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
# 
# Return the fewest number of coins that you need to make up that amount. If
# that amount of money cannot be made up by any combination of the coins,
# return -1.
# 
# You may assume that you have an infinite number of each kind of coin.
# 
# 
# Example 1:
# 
# 
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# 
# 
# Example 2:
# 
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# 
# Example 3:
# 
# 
# Input: coins = [1], amount = 0
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        You are given an integer array coins representing coins of different 
        denominations and an integer amount representing a total amount of money.
       
        Return the fewest number of coins that you need to make up that amount. 
        If that amount of money cannot be made up by any combination of the coins, return -1.
        
        You may assume that you have an infinite number of each kind of coin.

        Algorithm:
            1. Initialize a list `dp` of size `amount + 1` with all values set to infinity, 
                except `dp[0]` which is set to 0.
            2. Iterate through each amount from 1 to `amount`.
            3. For each coin in `coins`, update `dp[i]` as the minimum of `dp[i]` and 
                `dp[i - coin] + 1` if `i - coin >= 0`.
            4. Return `dp[amount]` if it is not infinity, otherwise return -1.
        
        Args:
            coins (List[int]): The list of coin denominations.
            amount (int): The total amount of money to make up.

        Returns:
            int: The fewest number of coins needed to make up the amount, or -1 if it is not possible.
        
        @complexity:
            Time: T(m, n) = O(m * n); where m is the amount and n is the number of coins.
            Space: S(m) = O(m); where m is the amount.
        """
        # dp array to store the minimum number of coins needed for each amount
        dp = [-1] * (amount + 1)
        dp[0] = 0

        # iterate through each amount from 1 to the target amount
        # for each amount, try using each coin to see if it leads to a smaller number of coins
        for a in range(1, amount + 1):
            for c in coins:
                # check if the remaining amount after using the current coin is non-negative
                if a - c >= 0:
                    # update dp[a] if using the current coin results in a smaller number of coins
                    if dp[a - c] != -1:
                        if dp[a] == -1:
                            dp[a] = 1 + dp[a - c]
                        else:
                            dp[a] = min(dp[a], 1 + dp[a - c]) # recurrence relation
        return dp[amount]
# @lc code=end

