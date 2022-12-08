'''
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum 
and return its sum.

A subarray is a contiguous part of an array.


Brute force (Cubic solution): 
compute contiguous subarray for ever element in the array.

for i = 0 to n - 1:
    for j = i to n - 1:
        for k = i to j:
            compute contiguous sum

Time complexity: T(n) = O(n**3)

Quadratic solution:
for i = 0 to n - 1:
    for j = i to n - 1:
        currentSum + nums[j]

Time complexity: T(n) = O(n**2)

Q: Do we have to start at every single element and compute every single subarray?
A: No, we can use our knowledge of what a 'maximum subarray' is to find a
temporal shortcut (shorter time spent computing the answer).

We can tell that negative numbers don't positively contribute to maximizing our subarrays.
A negative prefix can be ignored. This is what we want the computer to
ask itself: 

1. Does a negative prefix outweigh the current value?
2. Does the next elements in our nums array outweigh the current sum of our 
subarray?

This is a sliding window solution in linear time.
for i = 0 to n - 1:
    evaluate elements after the current and before by:
    1. removing negative prefix by shifting left pointer when negative "sliding window"
    2. keep incrementing right pointer to evaluate the max contiguous subarray
    3. stop condition of right pointer is the maximum value between the current contiguous sum
        and the previous maximum contiguous sums that have been computed at each indexed element

Time complexity: T(n) = O(n)
'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxContigSubArray = nums[0]
        currContigSum = 0
        n = len(nums)
        for i in range(0, n):
            if currContigSum < 0:
                # if less than zero reset the sum to zero to get rid of negative prefixes
                currContigSum = 0
            currContigSum += nums[i]
            maxContigSubArray = max(maxContigSubArray, currContigSum)
        return maxContigSubArray

