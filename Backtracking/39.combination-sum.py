#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (76.48%)
# Likes:    21369
# Dislikes: 549
# Total Accepted:    3.4M
# Total Submissions: 4.4M
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen
# numbers sum to target. You may return the combinations in any order.
# 
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen
# numbers is different.
# 
# The test cases are generated such that the number of unique combinations that
# sum up to target is less than 150 combinations for the given input.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple
# times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# 
# 
# Example 3:
# 
# 
# Input: candidates = [2], target = 1
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Given an array of distinct integers candidates and a target integer target, 
        return a list of all unique combinations of candidates where the chosen numbers 
        sum to target. You may return the combinations in any order.

        The same number may be chosen from candidates an unlimited number of times.
        Two combinations are unique if the frequency of at least one of the chosen numbers is different.

        The test cases are generated such that the number of unique combinations that 
        sum up to target is less than 150 combinations for the given input.

        Algorithm:
            1. Sort the candidates array to facilitate pruning of the search space.
            2. Use a backtracking approach to explore all possible combinations of candidates.
            3. For each candidate, recursively explore the possibility of including it in the current combination.
            4. If the current combination sums to the target, add it to the result list.
            5. If the current combination exceeds the target, backtrack and try the next candidate.

        Args:
            candidates (List[int]): An array of distinct integers.
            target (int): The target sum for the combinations.
        
        Returns:
            List[List[int]]: A list of all unique combinations that sum to the target.
        
        @complexity:
            time T(n) = O(2^n) in the worst case, where n is the number of candidates.
            space S(n) = O(n) for the recursion stack and the result list.
        """
        res = []
        # Sorting lets us stop as soon as a candidate exceeds the remainder.
        candidates.sort()

        def backtrack(remaining, combo, start):
            # A zero remainder means the current combination is complete.
            if remaining == 0:
                res.append(list(combo))
                return

            # Start at the current index to allow repeated candidates while
            # preventing duplicate combinations in a different order.
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break

                # Choose the candidate, explore, then undo the choice.
                combo.append(candidates[i])
                backtrack(remaining - candidates[i], combo, i)
                combo.pop()

        # Explore all valid combinations starting with an empty combination.
        backtrack(target, [], 0)
        return res
        
# @lc code=end

