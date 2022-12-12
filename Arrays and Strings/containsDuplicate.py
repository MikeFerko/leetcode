'''
Given an integer array nums, return true if any value 
appears at least twice in the array, and return false 
if every element is distinct.

1. Brute force compare every element of the array to every other element

T(n) = O(n**2)
S(n) = O(1)

2. Two pointers:
T(n) = O(nlogn)
S(n) = O(1)

3. Hash Set (use extra memeory for a faster result):

T(n) = O(n)
S(n) = O(n)


'''

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        return False
