#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        list1 : input of first linked list for merger
        list2 : input of 2nd linked list for merger
        dummy : dummy node whose dummy.next will be the head of the output merged linked list

        p1 -> points within linked list 1
        p2 -> points within linked list 2
        p3 -> points within the merged linked list called dummy.next

        Algorithm: Use a dummy node to initialize the merged linked list. use 2 pointers 
        to point to the head of each linked list up for merger. Iterate through both linked lists while 
        they are both not null. Add the missing tail of the remaining linked list. Return the dummy.next 
        as the head of the merged linked list.

        time T(n, m) = O(n * m) -> where n is the length of linked list 1 and m is the length of linked list 2
        space S(n, m) = O(n + m) -> store the whole of both linked lists into one larger linked list
        '''
        
        # use a dummy node to start the merged linked list
        # and point to the head of the merged linked list
        # for returning the merged linked list
        dummy = ListNode()

        # two pointers p1 in linked list 1 and p2 in linked list 2
        p1, p2 = list1, list2

        # 3rd pointer in dummy linked list
        p3 = dummy

        # while p1 or p2 is not null in linked list 1 and 2 respectively move up respective linked list
        # and move p3 after assigning linked list next node in dummy linked list
        while p1 and p2:
            if p1.val <= p2.val:
                p3.next = p1
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next
            p3 = p3.next
        
        # include the missed node at the end
        # since our loop termination condition makes us end before both linked list tails are reached
        # in which case we would add the existing tail - 1 so that p1 and p2 reach the tail
        if p1:
            p3.next = p1
        else:
            p3.next = p2
        
        return dummy.next
        

            
        
