#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

from typing import List

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Engineering vector algebra defines n as the row directional vector
        and m as the col directional vector with i, j respectively. In the problem
        statement these are flipped.

        grid : input/output grid of zeroes and ones and twos -> replace 1s with twos if 1 is in cardinal to a 2

        Algorithm: count number of fresh and number of rotten oranges. Add rotten oranges to the queue.
        dfs/bfs from rotten oranges and check if they are fresh and in boundary of matrix. If so, decrement the fresh count
        add rotten oranges to the queue and replace the value at that searched grid node to a rotten orange value of 2.
        Each time we iterate a rotten cycle we add a minute to the time counter. If fresh count is zero after searching
        the whole matrix for rotting all the fresh oranges we can return the time otherwise. Return -1 as a flag to indicate
        that all adjacent fresh oranges have been rotted, but there is still more fresh oranges. So a time cannot be accomplished.

        time T(n,m) = O(n * m) -> proportional to the size of the gridrix
        space S(n) = O(1) -> no extra storage required. Since we are just modifying the original matrix.
        '''


        n = len(grid) # row length
        m = len(grid[0]) # col lenth
        time, fresh = 0, 0
        visited = [[False for j in range(0, m)] for i in range(0, n)]
        
        queue = []
        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))

        # movement vector
        # up/down/left/right
        dRow = [0,0,-1,1] 
        dCol = [-1,1,0,0]
        
        while len(queue) > 0 and fresh > 0:
            for item in range(0, len(queue)):
                currentNode = queue[0]
                queue.remove(queue[0])
                i = currentNode[0]
                j = currentNode[1]

                for _ in range(0, 4):
                    newi = i + dRow[_]
                    newj = j + dCol[_]

                    if (0 <= newi <= n - 1 and 0 <= newj <= m - 1) and grid[newi][newj] == 1:
                        grid[newi][newj] = 2
                        queue.append((newi, newj))
                        fresh -= 1
            time += 1

        if fresh == 0:
            return time
        else:
            return -1
# @lc code=end

