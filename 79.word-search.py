#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (47.31%)
# Likes:    17988
# Dislikes: 762
# Total Accepted:    2.7M
# Total Submissions: 5.5M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# 
# Example 1:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
# 
# 
# 
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
# 
#

# @lc code=start
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Given an m x n grid of characters board and a string word, 
        return true if word exists in the grid. 

        The word can be constructed from letters of sequentially adjacent cells, 
        where adjacent cells are horizontally or vertically neighboring. 
        The same letter cell may not be used more than once.
        
        Algorithm:
            1. Iterate through the board and find the first character of the word.
            2. If the first character is found, perform a depth-first search (DFS) to find the next character in the word.
            3. If the next character is found, continue the DFS until the entire word is found or all possibilities are exhausted.

        Args:
            board (List[List[str]]): 2D grid of characters
            word (str): The word to search for in the grid

        Returns:
            bool: True if the word exists in the grid, False otherwise

        @complexity:
            Time: T(m, n, L) = O(m * n * 3^L), where m is the number of rows, n is the number 
            of columns, and L is the length of the word.
            Space: S(m, n, L) = O(L), where L is the length of the word (for the recursion stack).    
        """
        
        def dfs(i: int, j: int, k: int) -> bool:
            if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            
            # Mark the cell as visited by replacing it (in place) with a dp placeholder
            temp = board[i][j]
            board[i][j] = '#'
            
            # Explore all four directions (up, down, left, right)
            found = (dfs(i + 1, j, k + 1) or 
                     dfs(i - 1, j, k + 1) or 
                     dfs(i, j + 1, k + 1) or 
                     dfs(i, j - 1, k + 1))
            
            # Restore the cell's original value
            board[i][j] = temp
            
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        
        return False

        
# @lc code=end

