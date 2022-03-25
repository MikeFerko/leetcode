'''
152.

Dynamic programming problem

Given an integer array nums, find a contiguous non-empty subarray
within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit 
integer.

A subarray is a contiguous subsequence of the array.

brute force: Try every single combination of subarrays and see what the largest product would be
T(n) = O(n**2) -> check n patterns across the array for n elements


solution: 
1. Have the storage S(n) keep track of the maximum and minimum product values
2. Reset the maximum and minimum values to a neutral value (1) when a zero element
exists in the nums array to handle zero value edge case

Time Complexity: T(n) = O(n)
Space Complexity: S(n) = O(1) 

# using single stored values not an array, so the storage is constant
'''

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        currContigProdMin, currContigProdMax = 1,1
        n = len(nums)
        for i in range(0, n):

            # if the element in nums array has a value of zero at i reset the
            # contiguous product min and max to 1 each
            if nums[i] == 0:
                currContigProdMin, currContigProdMax = 1,1
                continue
            # this is due to a bug where the product wasn't being caluclated before the min/max was calculated
            tempProd = nums[i] * currContigProdMax 
            # maximum/minimum will be one of three values when iterating down the array:
            # 1. the current maximum contiguous product times the nums array element at i
            # 2. the current minimum cintiguous product times the nums array element at i
            # 3. the nums array element at i
            currContigProdMax = max(tempProd, nums[i] * currContigProdMin, nums[i])
            currContigProdMin = min(tempProd, nums[i] * currContigProdMin, nums[i])
            result = max(result, currContigProdMax, currContigProdMin)
        return result