#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

from typing import List

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        find the sum of two elements in numbers array that add up to
        a target value

        l : left pointer
        r : right pointer
        target : target value we are searching for a sum to equal
        numbers : input array sorted in ascending order

        1. apply binary search starting from the leftmost and rightmost values
        sum together and compare to target.
        2. If sum is less than target move the left pointer up
        3. If sum is greater than target move the right pointer down
        4. otherwise the sum is equal to the target 
        5. return the indices of the two value sum each added by one, who knows why
        6. we are guaranteed a target two sum, but if we weren't we would return an empty array

        time T(n) = O(n) -> search the entire array
        space S(n) = O(1) -> we only store indices and reevaluate those indices
        '''
        n = len(numbers)
        l, r = 0, n - 1
        while l < r:
            __sum = numbers[l] + numbers[r]
            if target > __sum:
                l += 1
            elif target < __sum:
                r -= 1
            else:
                return [l + 1, r + 1]            
        return []
# @lc code=end

