#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

from typing import List

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        global rowLength
        global colLength
        global visited
        rowLength = len(grid)
        colLength = len(grid[0])
        visited = [[False for j in range(0, colLength)] for i in range(0, rowLength)]
        maxIsland = 0

        for i in range(0, rowLength):
            for j in range(0, colLength):

                if grid[i][j] == 1:
                    maxIsland = max(maxIsland, self.dfs(grid, row = i, col = j))

                else:
                    visited[i][j] = True # mark all zeroes as True
        
        return maxIsland
    
    def isValid(self, grid: List[List[int]], row: int, col: int) -> bool:
        # boundary check on rows and cols
        if row < 0 or row > rowLength - 1 or col < 0 or col > colLength - 1:
            return False
        
        # check if the grid is on the island or not
        if grid[row][col] != 1:
            return False

        # otherwise return if the node has or has not been visited
        # if the node has not been visited we can return True 
        # If marked visited True return False
        return not visited[row][col]

    def dfs(self, grid: List[List[int]], row: int, col: int) -> int: 
        global dRow
        global dCol
        islandSize = 0

        # movement vectors up/down/left/right
        dRow = [0,0,-1,1]
        dCol = [1,-1,0,0]

        stack = []
        stack.append([row, col])

        while len(stack) > 0:
            currentNode = stack[len(stack) - 1]
            stack.remove(stack[len(stack) - 1])
            row = currentNode[0]
            col = currentNode[1]

            if self.isValid(grid, row, col):
                islandSize += 1
                visited[row][col] = True

                for _ in range(0, 4):
                    adjRow = row + dRow[_]
                    adjCol = col + dCol[_]
                    stack.append([adjRow, adjCol])
        return islandSize
        
                

# @lc code=end

