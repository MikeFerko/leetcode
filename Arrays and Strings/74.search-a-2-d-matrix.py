#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

from typing import List

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        matrix : input mutable array of array of integers -> could easily be an image of sorted pixel values
        target : integer value to search in 2d matrix
        output is a returned boolean True/False of if the value exists in our 2d matrix input

        Algorithm: binary search rows based on first and last value in mid row.
        Perform a 2nd binary search in the found mid row that could contain the value else return False if
        we have run out of bounds in the matrix. If the value is found in the 2nd binary search of the found row
        we can return True to say the value is in our matrix else return False to say the found row does not contain
        the target value.

        time T(m,n) = O(lg(m * n)) -> lg is log base 2
        space S(m, n) = O(1) -> no added storage besides what is presented and only constants are used.
        '''
        m = len(matrix) # rows
        n = len(matrix[0]) # columns

        top, bottom = 0, m - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break # search that row
        
        if (top > bottom): # if the bottom goes past top or vice versa then our value is not in the matrix
            return False # we could also easily change this to a flag if we were searching for a pixel or row/col index
        row = (top + bottom) // 2 # mid row found after first binary search of rows
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False # if we go through the whole row found and the value is not there just return false/flag

# @lc code=end

