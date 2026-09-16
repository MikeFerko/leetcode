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

        Algorithm:
            1. Initialize a stack to keep track of indices of temperatures.
            2. Initialize an answer array with zeros.
            3. Iterate through the temperatures:
                a. While the stack is not empty and the current temperature is greater
                   than the temperature at the index stored at the top of the stack:
                    i. Pop the index from the stack.
                    ii. Calculate the difference between the current index and the popped index,
                        and store it in the answer array at the popped index.
                b. Push the current index onto the stack.
            4. Return the answer array.

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
