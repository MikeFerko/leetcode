#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (55.11%)
# Likes:    17976
# Dislikes: 1620
# Total Accepted:    5.4M
# Total Submissions: 9.8M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given head, the head of a linked list, determine if the linked list has a
# cycle in it.
# 
# There is a cycle in a linked list if there is some node in the list that can
# be reached again by continuously following the next pointer. Internally, pos
# is used to denote the index of the node that tail's next pointer is connected
# to. Note that pos is not passed as a parameter.
# 
# Return true if there is a cycle in the linked list. Otherwise, return
# false.
# 
# 
# Example 1:
# 
# 
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to
# the 1st node (0-indexed).
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to
# the 0th node.
# 
# 
# Example 3:
# 
# 
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
# 
# 
# 
# Constraints:
# 
# 
# The number of the nodes in the list is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked-list.
# 
# 
# 
# Follow up: Can you solve it using O(1) (i.e. constant) memory?
# 
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Given head, the head of a linked list, determine if the 
        linked list has a cycle in it.

        There is a cycle in a linked list if there is some node 
        in the list that can be reached again by continuously 
        following the next pointer. Internally, pos is used to denote 
        the index of the node that tail's next pointer is connected to. 
        Note that pos is not passed as a parameter.

        Return true if there is a cycle in the linked list. Otherwise, 
        return false.

        Approach:
            Use `Floyd's Cycle detection` using a `tortoise` and a `hair` two
            pointer solution. Init slow and fast to head. Loop over fast and fast.next != None.
            increment slow by 1 node and fast by 2. If slow and fast hit the same node
            we have a cycle. If fast reaches the end of the list or fast.next reaches the end
            of the singly linked list then we won't have a cycle. Other solution would be to
            put it in a set, but that adds O(m) space complexity where m is the length of the set
            of nodes.
        
        Args:
            head (Optional[ListNode]): The start of the linked list input
        
        Returns:
            bool: True if a cycle exists in the linked list otherwise False.
        
        @complexity:
            Time: T(n) = O(n), worst case where n is the length of the linked list and
            we travel down the entire length.
            Space: S(n) = O(1), The only storage is the input and two locations in the
            linked list. Storage is constant space.       
        """
        slow = fast = head # tortoise, hair init
        while fast and fast.next: # loop terminates @ either None
            # slow trails fast, so never None here, but add a type narrowing assertion
            assert slow is not None
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
        
# @lc code=end

