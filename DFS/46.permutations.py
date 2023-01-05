#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

from typing import List

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        In mathematics, a permutation of a set is, loosely speaking, an arrangement of its members into a sequence or linear order, 
        or if the set is already ordered, a rearrangement of its elements.

        permutation formula:
        nPr = n! / (n - r)!

        time T(n) = O(nPr)
        space S(n) = O(nPr)
        '''
        perms = []
        def backtrack(nums: List[int], path: List[int]):
            if not nums:
                perms.append(path)
                return
            n = len(nums)
            for i in range(0, n):
                currentNode = nums[:i] + nums[i+1:]
                currentPath = path + [nums[i]]
                backtrack(currentNode, currentPath)

        backtrack(nums, [])
        return perms


# @lc code=end

