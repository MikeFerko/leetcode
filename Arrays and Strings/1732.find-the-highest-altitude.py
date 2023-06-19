#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n:int = len(gain); # calculating this before looping saves on time.
        currentAltitude:int = 0
        highestAltitude:int = 0

        '''
        using constants to keep track of previous and current net gains will allow us
        to solve this without using a net gain in altitude array of size n + 1
        '''
        for i in range(0, n):
            currentAltitude += gain[i]
            highestAltitude = max(highestAltitude, currentAltitude)
        
        '''
        base case we return the initialized value of 0, else we iterate over 1 to n - 1 elements of the array
        finding the current net altitude gain fand, previous net altitude gain and the highest altitude of the 
        biker. 
        '''
        return highestAltitude
        
# @lc code=end

