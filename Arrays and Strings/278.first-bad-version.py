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
        """
        Given n versions [1, n] where all versions after a bad one are also
        bad, find the first bad version using binary search on the
        isBadVersion API. Constraints: 1 <= bad <= n <= 2**31 - 1.

        Args:
            n (int): total number of versions

        Returns:
            int: the first bad version

        @complexity: Time: O(logn)
        @complexity: Space: O(1)
        """
        l, h = 1, n
        while l < h:
            mid = (l + h) // 2
            if isBadVersion(mid):
                h = mid
            else:
                l = mid + 1
        return l
            
                




# @lc code=end