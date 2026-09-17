#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (81.89%)
# Likes:    21160
# Dislikes: 391
# Total Accepted:    3.3M
# Total Submissions: 4M
# Testcase Example:  '[1,2,3]'
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Given an array nums of distinct integers, return all the possible permutations.

        Algorithm:
            1. Initialize an empty list 'result' to store all permutations.
            2. Define a recursive function 'backtrack' that takes the current 
               permutation and the remaining numbers as parameters.
            3. If there are no remaining numbers, add the current permutation 
               to the result list.
            4. Otherwise, iterate through the remaining numbers, and for each 
               number, call 'backtrack' with the updated current permutation 
               and remaining numbers.
            5. Return the result list containing all permutations.
        
        Args:
            nums (List[int]): A list of distinct integers.
        
        Returns:
            List[List[int]]: A list of all possible permutations of the input list.
        
        @complexity:
            Time: T(n) = O(n * n!) - There are n! permutations and generating each 
            permutation takes O(n) time.
            Space: S(n) = O(n * n!) - The space required to store all permutations.
        """
        result = []

        # Build each permutation by choosing one remaining number at a time.
        def backtrack(current_permutation: List[int], remaining_nums: List[int]):
            # A complete permutation is ready to be added to the results.
            if not remaining_nums:
                result.append(current_permutation)
                return

            # Try every remaining number in the next position.
            for i in range(len(remaining_nums)):
                next_num = remaining_nums[i]
                # Remove the chosen number before exploring the next step.
                new_remaining = remaining_nums[:i] + remaining_nums[i+1:]
                backtrack(current_permutation + [next_num], new_remaining)

        # Start with an empty permutation and all input numbers available.
        backtrack([], nums)
        return result
        
# @lc code=end

