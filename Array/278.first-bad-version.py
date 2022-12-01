#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        '''
        find the first bad version in an array of sorted versions
        that run from 0 up to n

        bad : int : our target version we are searching for
        l : int : low pointer
        h : int : high pointer
        mid : our middle pointer for binary search of our version

        Constraints: 1 <= bad <= n <= 2**31 - 1
        '''
        l, h = 1, n
        while l < h:
            mid = (l + h) // 2
            if isBadVersion(mid):
                h = mid
            else:
                l = mid + 1
        return l
            
                




# @lc code=end