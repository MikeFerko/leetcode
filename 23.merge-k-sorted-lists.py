#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (60.56%)
# Likes:    21622
# Dislikes: 801
# Total Accepted:    3.2M
# Total Submissions: 5.3M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# You are given an array of k linked-lists lists, each linked-list is sorted in
# ascending order.
# 
# Merge all the linked-lists into one sorted linked-list and return it.
# 
# 
# Example 1:
# 
# 
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6
# 
# 
# Example 2:
# 
# 
# Input: lists = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: lists = [[]]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 10^4.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        You are given an array of 'k' linked-lists, each linked-list is sorted in ascending order.

        Merge all the linked-lists into one sorted linked-list and return it.

        Algorithm:
            1. Initialize a min-heap.
            2. Push the head of each linked list into the heap.
            3. Pop the smallest element from the heap and add it to the merged list.
            4. If the popped element has a next node, push it into the heap.
            5. Repeat steps 3-4 until the heap is empty.
            6. Return the merged list.
        
        Args:
            lists (List[Optional[ListNode]]): A list of k sorted linked-lists.

        Returns:
            Optional[ListNode]: The head of the merged sorted linked-list.
        
        @complexity:
            Time: T(n, k) = O(n log k), where n is the total number of nodes and k is the number of linked-lists.
            Space: S(n), where n is the total number of nodes, for the min-heap.
        """

        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next
# @lc code=end

