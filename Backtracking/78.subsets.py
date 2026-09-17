#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (82.30%)
# Likes:    19537
# Dislikes: 352
# Total Accepted:    3.3M
# Total Submissions: 3.9M
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 
# 
# Example 2:
# 
# 
# Input: nums = [0]
# Output: [[],[0]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums of unique elements, return all possible 
        subsets (the power set).

        Algorithm:
            1. Initialize an empty list 'result' to store all subsets.
            2. Define a recursive function 'backtrack' that takes the current 
               index and the current subset as parameters.
            3. In each call of 'backtrack', append the current subset to 'result'.
            4. Iterate through the elements of nums starting from the current index.
            5. For each element, include it in the current subset and recursively 
               call 'backtrack' with the next index.
            6. After returning from recursion, remove the last element to backtrack 
               and explore other subsets.
            7. Start the recursion with an empty subset and index 0.
            8. Return the 'result' containing all subsets.

        Args:
            nums (List[int]): An integer array of unique elements.
        
        Returns:
            List[List[int]]: A list of all possible subsets of the input array.
        
        @complexity:
            Time: T(n) = O(2^n), where n is the length of nums. Each element can either 
            be included or excluded from a subset, leading to 2^n possible subsets.
            Space: S(n) = O(n) for the recursion stack and O(2^n) for storing all subsets.
        """
        result = []

        def backtrack(start: int, current_subset: List[int]):
            # Append a copy of the current subset to the result
            result.append(current_subset[:])
            # Iterate through the remaining elements
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                current_subset.append(nums[i])
                # Move on to the next element
                backtrack(i + 1, current_subset)
                # Backtrack by removing the last element added
                current_subset.pop()

        # Start the backtracking with an empty subset and starting index 0
        backtrack(0, [])
        return result
        
# @lc code=end

