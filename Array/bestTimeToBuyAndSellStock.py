'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

want to: Buy low and sell high

Use two pointers for day 1 and day 2
find current profit & keep track of max profit for all the current profits.
L = Buy
R = Sell
current profit = prices[R] - prices[L] 

memory/space: S(n) = O(1) didn't use any other array besides the one
time: T(n) = O(n) scan through the array one time with two pointers.
'''

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left = buy, right = Sell
        maxP = 0

        while r < len(prices):
            # is the buy/sell combination profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r # the right pointer is looking at a lower buying price
            r += 1
        return maxP