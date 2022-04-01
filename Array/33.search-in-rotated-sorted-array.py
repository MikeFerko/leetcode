#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

'''
* Note: 
1. log is the common logarithm base 10 from the decimal number system
2. ln is the natural logarithm base e
3. lg is the binary logarithm base 2 from the binary number system

Need a time complexity of O(lg n)
binary search using left middle and right pointers
i.e. use similar technique as in 153.

if  1. nums[left] <= nums[middle] < target -> left portion asc and target out of bounds
    2. target < nums[left] <= nums[target] -> left porton asc and target out of bounds
    3. nums[middle] < target < nums[left]: -> large value rotated to front of array and target out of bounds 
    search right
else:
    search left
'''

from typing import List
import math
import time

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while (left <= right):
            middle = math.floor((left + right) // 2) 
            
            # loop terminate if we find the target value at
            # any of our pointers
            if (target == nums[middle]):
                return middle
            # search the right portion
            elif (nums[left] <= nums[middle] < target or \
                target < nums[left] <= nums[middle] or \
                nums[middle] < target < nums[left]):
                left = middle + 1
            else:
                right = middle - 1
        return -1

# list_ = [8,1,2,3,4,5,6,7]
# target = 6
# sol = Solution()
# print(sol.search(list_,target))

# @lc code=end

