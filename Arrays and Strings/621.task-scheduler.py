#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#
# https://leetcode.com/problems/task-scheduler/description/
#
# algorithms
# Medium (63.03%)
# Likes:    12115
# Dislikes: 2245
# Total Accepted:    1M
# Total Submissions: 1.6M
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# You are given an array of CPU tasks, each labeled with a letter from A to Z,
# and a number n. Each CPU interval can be idle or allow the completion of one
# task. Tasks can be completed in any order, but there's a constraint: there
# has to be a gap of at least n intervals between two tasks with the same
# label.
# 
# Return the minimum number of CPU intervals required to complete all tasks.
# 
# 
# Example 1:
# 
# 
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# 
# Output: 8
# 
# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A ->
# B.
# 
# After completing task A, you must wait two intervals before doing A again.
# The same applies to task B. In the 3^rd interval, neither A nor B can be
# done, so you idle. By the 4^th interval, you can do A again as 2 intervals
# have passed.
# 
# 
# Example 2:
# 
# 
# Input: tasks = ["A","C","A","B","D","B"], n = 1
# 
# Output: 6
# 
# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
# 
# With a cooling interval of 1, you can repeat a task after just one other
# task.
# 
# 
# Example 3:
# 
# 
# Input: tasks = ["A","A","A", "B","B","B"], n = 3
# 
# Output: 10
# 
# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle
# -> idle -> A -> B.
# 
# There are only two types of tasks, A and B, which need to be separated by 3
# intervals. This leads to idling twice between repetitions of these tasks.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= tasks.length <= 10^4
# tasks[i] is an uppercase English letter.
# 0 <= n <= 100
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        You are given an array of CPU tasks, each labeled with a letter
        from A to Z, and a number n. Each CPU interval can be idle or allow 
        the completion of one task. Tasks can be completed in any order, 
        but there's a constraint: there has to be a gap of at least n 
        intervals between two tasks with the same label.

        Return the minimum number of CPU intervals required to complete all tasks.

        Using a queue to track the frequency of each task.
        
        Args:
            tasks (List[str]): array of CPU tasks
            n (int): the number of intervals between two tasks with the same label

        Returns:
            int: the minimum number of CPU intervals required to complete all tasks
        
        @complexity: Time: O(n)
        @complexity: Space: O(n)
        """
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        # sort ascending so the most frequent task ends up at freq[25]
        freq.sort()
        max_freq = freq[-1]

        # skeleton: the most frequent task needs (max_freq - 1) gaps of size n
        # between its own repetitions, e.g. A _ _ A _ _ A
        idle_slots = (max_freq - 1) * n

        # fill those gaps with every OTHER task (indices 0..24, not 25).
        # each other task can occupy at most (max_freq - 1) of the gap slots
        # any more and it would need its own cooldown gaps too.
        # NOTE: This must start at 24, not 25. freq[25] is the
        # max-frequency task itself, and it can't fill its own cooldown gaps;
        # including it here double-subtracted capacity and undercounted the
        # answer (e.g. ["A","A","A","B","B","B"], n=2 returned 6 instead of 8).
        for i in range(24, -1, -1):
            idle_slots -= min(freq[i], max_freq - 1)

        # if other tasks overfilled the gaps, idle_slots goes negative here,
        # and max() below just falls back to the total task count.
        return max(len(tasks), idle_slots + len(tasks))
        
# @lc code=end

