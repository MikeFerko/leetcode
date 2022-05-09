#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Example:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Iterative:
Time Complexity: T(n) = O(n) - iterative solution - iterate through the length of linked list
Space Complexity: S(n) = O(1) - each iteration we store the same amount into memory.

Recursvie:
Time Complexity: T(n) = O(n) - iterative solution - iterate through the length of linked list
Space Complexity: S(n) = O(n) - each iteration we store the same amount into memory.
'''
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head

        while current != None:
            next = current.next # store the next in memory # 2
            current.next = previous # reverse the link in the list # none
            previous = current # identify the new previous node # head 1
            current = next # 2
        return previous
    
    # # recursive solution
    # def recursiveReverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head:
    #         return None
        
    #     newHead = head
    #     if head.next:
    #         newHead = self.recursiveReverseList(head.next)
    #         head.next.next = head
    #     # set the head of linked list
    #     head.next = None
    #     return newHead
# @lc code=end

