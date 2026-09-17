#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (64.32%)
# Likes:    25385
# Dislikes: 627
# Total Accepted:    4.5M
# Total Submissions: 6.9M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
# 
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
# 
# 
# Example 1:
# 
# 
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given a 2D grid map of '1's (land) and '0's (water),
        count the number of islands. An island is surrounded
        by water and is formed by connecting adjacent lands
        horizontally or vertically. You may assume all four
        edges of the grid are all surrounded by water.

        Algorithm:
            1. Initialize a counter for the number of islands.
            2. Iterate through each cell in the grid.
            3. If a cell contains '1', increment the counter and
            perform a depth-first search to mark all connected '1's as a visited part of the same island.
            4. Return the number of islands found after traversing the entire grid.

        Note: DFS is done iteratively with an explicit stack rather than recursively.
        Constraints allow up to 300x300 = 90,000 cells, and a single snaking island
        could recurse 90,000 levels deep, exceeding Python's default recursion limit
        (1000) and crashing with a RecursionError. An explicit stack has no such ceiling.

        Args:
            grid (List[List[str]]): A 2D list representing the map of '1's (land) and '0's (water).

        Returns:
            int: The number of islands in the grid.

        @complexity:
            Time Complexity: T(m, n) = O(m * n), where m is the number of rows and n is the number of columns in the grid. Each cell is visited once.
            Space Complexity: S(m, n) = O(m * n) in the worst case for the explicit stack
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def dfs(r, c):
            # Mark the starting cell as visited and explore its island iteratively.
            grid[r][c] = '0'
            stack = [(r, c)]

            while stack:
                cur_r, cur_c = stack.pop()

                for next_r, next_c in ((cur_r + 1, cur_c), (cur_r - 1, cur_c),
                                        (cur_r, cur_c + 1), (cur_r, cur_c - 1)):
                    # Skip water or coordinates outside the grid.
                    if 0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == '1':
                        # Mark as visited before pushing to avoid queuing the same cell twice.
                        grid[next_r][next_c] = '0'
                        stack.append((next_r, next_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    # An unvisited land cell starts a new island.
                    num_islands += 1
                    dfs(r, c)

        return num_islands
        
# @lc code=end

