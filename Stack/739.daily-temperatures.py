#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

from typing import List

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Given an array of integers temperatures represents the daily temperatures,
        return an array answer such that answer[i] is the number of days you have
        to wait after the ith day to get a warmer temperature. If there is no future
        day for which this is possible, keep answer[i] == 0 instead.

        Args:
            temperatures (List[int]): array of daily temperatures

        Returns:
            List[int]: array of days to wait to get a warmer temperature

        @complexity: Time: O(n)
        @complexity: Space: O(n)
        """
        n = len(temperatures)
        # plain list beats deque here: we only ever push/pop the right end,
        # and list.append/pop have lower per-op overhead than deque for that
        stack = []  # indices with temperatures we haven't found a warmer day for yet
        answer = [0] * n

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)

        return answer
# @lc code=end
