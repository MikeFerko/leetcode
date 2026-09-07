#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        """
        Given an array gain of net altitude changes between consecutive
        points, return the highest altitude reached, starting from an
        altitude of 0. Track a running current altitude and the highest
        altitude seen so far, using constants instead of building a
        separate altitude array of size n + 1.

        Args:
            gain (List[int]): net altitude change between consecutive points

        Returns:
            int: the highest altitude reached

        @complexity: Time: O(n)
        @complexity: Space: O(1)
        """
        n:int = len(gain); # calculating this before looping saves on time.
        currentAltitude:int = 0
        highestAltitude:int = 0

        for i in range(0, n):
            currentAltitude += gain[i]
            highestAltitude = max(highestAltitude, currentAltitude)

        return highestAltitude
        
# @lc code=end

