#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (60.90%)
# Likes:    8888
# Dislikes: 1875
# Total Accepted:    863K
# Total Submissions: 1.4M
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# There is an m x n rectangular island that borders both the Pacific Ocean and
# Atlantic Ocean. The Pacific Ocean touches the island's left and top edges,
# and the Atlantic Ocean touches the island's right and bottom edges.
# 
# The island is partitioned into a grid of square cells. You are given an m x n
# integer matrix heights where heights[r][c] represents the height above sea
# level of the cell at coordinate (r, c).
# 
# The island receives a lot of rain, and the rain water can flow to neighboring
# cells directly north, south, east, and west if the neighboring cell's height
# is less than or equal to the current cell's height. Water can flow from any
# cell adjacent to an ocean into the ocean.
# 
# Return a 2D list of grid coordinates result where result[i] = [ri, ci]
# denotes that rain water can flow from cell (ri, ci) to both the Pacific and
# Atlantic oceans.
# 
# 
# Example 1:
# 
# 
# Input: heights =
# [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans,
# as shown below:
# [0,4]: [0,4] -> Pacific Ocean 
# [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
# [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
# [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
# [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean 
# [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
# [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean 
# ⁠      [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the
# Pacific and Atlantic oceans.
# 
# 
# Example 2:
# 
# 
# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and
# Atlantic oceans.
# 
# 
# 
# Constraints:
# 
# 
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 10^5
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        There is an `m x n` rectangular island that borders both the `Pacific Ocean` 
        and `Atlantic Ocean`. The `Pacific Ocean` touches the island's left and top edges, 
        and the `Atlantic Ocean` touches the island's right and bottom edges.

        The island is partitioned into a grid of square cells. You are given an `m x n`
        integer matrix `heights` where `heights[r][c]` represents the height above sea
        level of the cell at coordinate `(r, c)`.

        The island receives a lot of rain, and the rain water can flow to neighboring
        cells directly north, south, east, and west if the neighboring cell's height
        is less than or equal to the current cell's height. Water can flow from any
        cell adjacent to an ocean into the ocean.

        Return a 2D list of grid coordinates `result` where `result[i] = [ri, ci]`
        denotes that rain water can flow from cell (ri, ci) to both the Pacific and
        Atlantic oceans.

        Algorithm:
            1. Initialize two sets, `pacific_reachable` and `atlantic_reachable`, 
                to keep track of the cells that can reach the Pacific and Atlantic oceans, respectively.
            2. Perform a Depth-First Search (DFS) or Breadth-First Search (BFS) from the 
                cells adjacent to the Pacific Ocean (top row and left column) and mark 
                all reachable cells in `pacific_reachable`.
            3. Perform a DFS or BFS from the cells adjacent to the Atlantic Ocean (bottom 
                row and right column) and mark all reachable cells in `atlantic_reachable`.
            4. The final result will be the intersection of `pacific_reachable` and 
                `atlantic_reachable`, which contains the coordinates of cells that can flow to both oceans.
            
        Args:
            heights (List[List[int]]): A 2D list representing the heights of the cells.
        
        Returns:
            List[List[int]]: A list of coordinates where water can flow to both oceans.
        
        @complexity:
            Time Complexity: T(m, n) = O(m * n), where m is the number of rows and n is the number of columns in the heights matrix.
            Space Complexity: S(m, n) = O(m * n) for the visited sets and the result list.
        """
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def reachable_from_ocean(starts):
            """Find cells reachable from an ocean by following nondecreasing heights."""
            reachable = set(starts)
            stack = list(starts)

            while stack:
                r, c = stack.pop()

                # Reverse the water-flow direction: from a cell, we may move to
                # a neighbor that is at least as high as the current cell.
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in reachable
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        reachable.add((nr, nc))
                        stack.append((nr, nc))

            return reachable

        # The Pacific touches the top and left edges.
        pacific_starts = {
            *[(0, c) for c in range(cols)],
            *[(r, 0) for r in range(rows)],
        }

        # The Atlantic touches the bottom and right edges.
        atlantic_starts = {
            *[(rows - 1, c) for c in range(cols)],
            *[(r, cols - 1) for r in range(rows)],
        }

        # A cell can reach both oceans when it is reachable from both edge sets.
        both = reachable_from_ocean(pacific_starts) & reachable_from_ocean(atlantic_starts)
        return [[r, c] for r, c in both]

# @lc code=end

