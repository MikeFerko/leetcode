#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Brute Force: Use a helper function to get the length of the whole singly linked list
        use ceiling division to find the middle of the length of the singly linked list
        and return that.
        
        fast and slow pointer algorithm: Use a fast and slow pointer so that the fast pointer iterates
        at 2x the speed of the slow pointer. The slow pointer will end at the middle of the linked list
        in optimal time. Return the slow pointer as the output

        Two cases to look at: 
        1. even length linked list
        2. odd length linked list
        
        head : input singly Linked List
        s : slow pointer
        f : fast pointer

        time T(n) = O(n/2) = O(n) -> traverse entire linked list
        space s(n) = O(1) -> constantly only storing the two linked lists in s and f
        '''
        s, f = head, head
        while f != None and f.next != None:
            s = s.next
            f = f.next.next
        return s


# @lc code=end

