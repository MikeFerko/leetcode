#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

from typing import List

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        Engineering vector algebra defines n as the row directional vector
        and m as the col directional vector with i, j respectively. In the problem
        statement these are flipped.

        mat : input/output matrix of zeroes and ones  -> replace 1s with distance to nearest zero

        Algorithm: mark all zeroes as visited and add to queue. Remove the first element from
        the queue and search in all 4 cardinal directions. If the next nodes is in the matrix boundaries
        and has not been visited -> replace it's value with the previous nodes value, mark that node as visited
        and add it to the end of the FIFO queue. 

        time T(n,m) = O(n * m) -> proportional to the size of the matrix
        space S(n) = O(n * m) -> stored an extra matrix to mark visited nodes
        We could just use the original matrix and use a flag value. For an O(1) space solution.
        '''


        n = len(mat) # row length
        m = len(mat[0]) # col lenth
        
        visited = [[False for j in range(0, m)] for i in range(0, n)]
        queue = []

        for i in range(0, n):
            for j in range(0, m):
                if mat[i][j] == 0:
                    visited[i][j] = True
                    queue.append((i, j))

        # movement vector
        # up/down/left/right
        dRow = [0,0,-1,1] 
        dCol = [-1,1,0,0]
        
        while len(queue) > 0:
            currentNode = queue[0]
            queue.remove(queue[0])
            i = currentNode[0]
            j = currentNode[1]

            for _ in range(0, 4):
                newi = i + dRow[_]
                newj = j + dCol[_]

                if (0 <= newi <= n - 1 and 0 <= newj <= m - 1) and not visited[newi][newj]:
                    mat[newi][newj] = mat[i][j] + 1
                    visited[newi][newj] = True
                    queue.append((newi, newj))
            
            
        return mat


                
# @lc code=end

