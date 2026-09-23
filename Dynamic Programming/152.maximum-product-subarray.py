#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (37.08%)
# Likes:    20853
# Dislikes: 847
# Total Accepted:    2.2M
# Total Submissions: 6M
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find a subarray that has the largest product,
# and return the product.
# 
# The test cases are generated so that the answer will fit in a 32-bit
# integer.
# 
# Note that the product of an array with a single element is the value of that
# element.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# The product of any subarray of nums is guaranteed to fit in a 32-bit
# integer.
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Given an integer array nums, find a subarray that has the 
        largest product, and return the product.

        The test cases are generated so that the answer will fit in a 32-bit integer.

        Note that the product of an array with a single element is 
        the value of that element.
        
        Algorithm:
            Use dynamic programming to keep track of the maximum and minimum products 
            ending at each position. The maximum product subarray ending at the current 
            position can be obtained by multiplying the current number with the maximum 
            or minimum product ending at the previous position, depending on the sign of 
            the current number. Keep track of the global maximum product while iterating 
            through the array.
        
        Args:
            nums (List[int]): The list of integers.

        Returns:
            int: The maximum product of a subarray.
        
        @complexity:
            Time: T(n) = O(n); where n is the length of the input list.
            Space: S(n) = O(1); constant extra space is used.
        """
        # edge case: empty array
        if not nums:
            return 0

        max_prod = min_prod = global_max = nums[0]

        # iterate through the array starting from the second element
        for n in nums[1:]:
            # if the current number is negative, swap the max and min products
            if n < 0:
                max_prod, min_prod = min_prod, max_prod
            # else n >= 0, continue with the current max and min products
            max_prod = max(n, max_prod * n)
            min_prod = min(n, min_prod * n)
            global_max = max(global_max, max_prod)

        return global_max

        
# @lc code=end

