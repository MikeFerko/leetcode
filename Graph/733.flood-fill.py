#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

from typing import List
# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        '''
        image: input 2d array of integers as pixel values
        sr: input source row -> i.e. which row to start at within the image
        sc: input source column -> i.e. which column to start at within the image
        color: input colour that we want to change all the starting pixels to this color

        Algorithm: dfs on pixels/nodes move in 4 cardinal directions up/down/left/right. Use a stack
        to keep track of the pixel locations and move in the image using a directional vector.
        pop and remove each pixel pair as we move. Extrapolate a valid pixel function to check
        each pixel is within the image boundaries. 
        If the pixel is the desired color don't visit that pixel.
        If the pixel is the desired color we can visit it.
        In which case change the color to the desired starting color and add the adjacent pixels.
        Invalid adjacent pixels won't be visited.

        time T(n) = O(m x n) -> wher m is the number of columns, n is the number of rows in the image
        space S(n) = O(m x n) -> store the whole image.

        i.e. more rows and columns then more time and space
        '''
        return self.dfs(image, sr, sc, color) # iterative implementation

    def isValid(self, image: List[List[int]], row: int, col: int) -> bool:  
        # if element is out of bounds
        if row < 0 or col < 0 or row > rowLength - 1 or col > colLength - 1:
            return False

        # if the element in our matrix has already been visited
        # if visited[col][row]:
        #     return False
        color = image[row][col]
        if color == newColor:
            return False            
        
        # otherwise, it may be visited
        return color == startingColor

    def dfs(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # make a mtrix to keep track of which nodes have been visited
        global rowLength
        global colLength
        # global visited
        global newColor
        global startingColor
        global dRow
        global dCol

        rowLength = len(image)
        colLength = len(image[0])
        # visited = [[False for i in range(0, rowLength)] for j in range(0, colLength)]
        newColor = color
        startingColor = image[sr][sc]

        # initialized the directional vectors to move in the image at each pixel/node
        # Initialize direction vectors
        # up/down/left/right
        dRow = [0, 0, -1, 1]
        dCol = [1, -1, 0, 0]

        # add source rows and source column for pixel location to the stack
        stack = []
        stack.append([sr, sc])

        while len(stack) > 0:
            # pop the top pair in the stack
            currentNode = stack[len(stack) - 1]
            stack.remove(stack[len(stack) - 1])
            row = currentNode[0]
            col = currentNode[1]

            # check if the current popped element is
            # a valid element
            if self.isValid(image, row, col):                
                # Mark the current element as visited
                # visited[row][col] = True
                image[row][col] = newColor

                # check the cardinal directions up/down/left/right
                for cd in range(0, 4):
                    adjRow = row + dRow[cd] # adjacent row
                    adjCol = col + dCol[cd] # adjacent col
                    stack.append([adjRow, adjCol]) # add possible nodes/pixels to visit in the image

        return image
# @lc code=end

