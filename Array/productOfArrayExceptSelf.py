'''
Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i]. 

The product of any prefix or suffix of nums is guaranteed to fit in a 
32-bit integer. 

You must write an algorithm that runs in O(n) time and without 
using the division operation.

Divide and conquer solution:

Divide the nums[i] array into a prefix and suffix.

For each value at pointer i in the array nums we want to compute the
prefix value for the product of all the numbers before nums[i] and
the suffix for the product of all the numbers after nums[i]. Then store
the prefix product values into the array answers at the current pointer i
and store all the suffix values by multiplying the current prefix stored in
the answers value at i with the suffix values.

Time complexity: T(n) = O(n)
Space complexity: S(n) = O(1) # didn't need prefix and suffix extra arrays.
'''

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) # caculating n before computation improves speed.
        answer = [1] * n # initial value of 1 for all values in output array
        prefix = 1        
        for i in range(0, n): # 0 up to n - 1
            answer[i] = prefix
            '''multiply the prefix with the current nums value
            to get the next prefix value
            '''
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1): # n - 1 down to 0
            answer[i] *= suffix # multiply the prefix and postfix together
            '''multiply the suffix with the current nums value
            to get the next suffix value
            '''
            suffix *= nums[i]
        # ... is the elipsis continuation of an array
        
        ''' 
        answer[i] = 
        prefix[i - 1] * ... * prefix[0] 
        * suffix[i + 1] * ... * suffix[n - 1]
        '''
        
        return answer
        
