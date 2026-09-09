#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (51.74%)
# Likes:    25046
# Dislikes: 920
# Total Accepted:    4.3M
# Total Submissions: 8.2M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given an array of intervals where intervals[i] = [starti, endi], merge all
# overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.
# 
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# 
# Example 3:
# 
# 
# Input: intervals = [[4,7],[1,4]]
# Output: [[1,7]]
# Explanation: Intervals [1,4] and [4,7] are considered overlapping.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
# 
# 
#

# @lc code=start

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Given an array of intervals where intervals[i] = [starti, endi],
        merge all overlapping intervals, and return an array of the 
        non-overlapping intervals that cover all the intervals in the input.
        Check each interval to see if it overlaps with any other interval.
        If it does, merge the intervals. Else, don't merge the 
        intervals as in the merge sort algorithm.

        Args:
            intervals (List[List[int]]): Array of intervals where intervals[i] = [starti, endi]

        Returns:
            List[List[int]]: Array of non-overlapping intervals that cover all the intervals in the input
        
        @complexity: Time: T(n) = O(nlogn)
        @complexity: Space: S(n) = O(n)
        """

        # stop short if we have one interval in intervals.
        if len(intervals) == 1:
            return intervals

        # sort the intervals based on their start values
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals by taking the maximum of the current interval and the previous
                # merged interval that overlaps with the current interval. Minimum is
                # not needed because the intervals are sorted.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
        
# @lc code=end

