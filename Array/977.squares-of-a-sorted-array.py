#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

from typing import List
# two pointers approach

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        nums : input array
        output : output array
        l : left pointer
        r : right pointer
        j : output array pointer

        compare left and right squares until the left pointer 
        is less than the right pointer
        '''
        n = len(nums)
        output = [0] * n
        l, r = 0, n - 1
        j = n - 1
        while r >= l:
            vall = nums[l] ** 2
            valr = nums[r] ** 2
            if vall > valr:
                output[j] = vall
                l += 1
            else:
                output[j] = valr
                r -= 1
            j -= 1
        return output


            
# @lc code=end

