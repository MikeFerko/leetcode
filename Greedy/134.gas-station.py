#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#
# https://leetcode.com/problems/gas-station/description/
#
# algorithms
# Medium (48.74%)
# Likes:    13790
# Dislikes: 1412
# Total Accepted:    1.5M
# Total Submissions: 3M
# Testcase Example:  '[1,2,3,4,5]\n[3,4,5,1,2]'
#
# There are n gas stations along a circular route, where the amount of gas at
# the i^th station is gas[i].
# 
# You have a car with an unlimited gas tank and it costs cost[i] of gas to
# travel from the i^th station to its next (i + 1)^th station. You begin the
# journey with an empty tank at one of the gas stations.
# 
# Given two integer arrays gas and cost, return the starting gas station's
# index if you can travel around the circuit once in the clockwise direction,
# otherwise return -1. If there exists a solution, it is guaranteed to be
# unique.
# 
# 
# Example 1:
# 
# 
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 +
# 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to
# station 3.
# Therefore, return 3 as the starting index.
# 
# 
# Example 2:
# 
# 
# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to
# the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 =
# 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you
# only have 3.
# Therefore, you can't travel around the circuit once no matter where you
# start.
# 
# 
# 
# Constraints:
# 
# 
# n == gas.length == cost.length
# 1 <= n <= 10^5
# 0 <= gas[i], cost[i] <= 10^4
# The input is generated such that the answer is unique.
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        There are n gas stations along a circular route, where the amount of 
        gas at the ith station is gas[i].

        You have a car with an unlimited gas tank and it costs cost[i] of gas 
        to travel from the ith station to its next (i + 1)th station. You begin 
        the journey with an empty tank at one of the gas stations.

        Given two integer arrays gas and cost, return the starting gas station's 
        index if you can travel around the circuit once in the clockwise direction, 
        otherwise return -1. If there exists a solution, it is guaranteed to be unique.
        
          Algorithm:
            1. Check that a solution is possible by comparing the total gas and total cost. If the total gas is less than the total cost, return -1.
            2. Initialize two variables: current_gas to track the current amount of gas in the tank, and start_index to track the starting gas station's index.
            3. Iterate through the gas and cost arrays:
                - For each station, update current_gas by adding the gas at the current station and subtracting the cost to travel to the next station.
                - If current_gas becomes negative, it means we cannot reach the next station from the current starting index. Therefore, update start_index to the next station (i + 1) and reset current_gas to 0.
            4. After iterating through all stations, return start_index as the starting gas station's index if a complete circuit is possible.
            
        Args:
            gas (List[int]): An array representing the amount of gas at each station.
            cost (List[int]): An array representing the cost of gas to travel to the next station.
        
        Returns:
            int: The starting gas station's index if a complete circuit is possible, otherwise -1.
        
        @complexity:
            Time complexity: T(n) = O(n), where n is the number of gas stations. We iterate through the gas and cost arrays once.
            Space complexity: S(n) = O(1), as we use a constant amount of extra space.
        """
        # check if a solution is possible by comparing total gas and total cost
        if sum(gas) < sum(cost):
            return -1

        current_gas = 0
        start_index = 0
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            print(f"Station {i}: Gas = {gas[i]}, Cost = {cost[i]}, Current Gas = {current_gas}")
            if current_gas < 0:
                start_index = i + 1
                current_gas = 0
        return start_index

# @lc code=end

