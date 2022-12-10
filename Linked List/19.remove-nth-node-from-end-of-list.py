#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Two Pointers Algorithm: We want the window length between the left and right pointer to be
        one greater than n so that when we shift the right pointer by n + 1
        and  the right pointer reaches the length of the linked list
        then the left pointer will be the previous node of the nth node from the
        end of the linked list. 

        We can then reassign the left.next to the node after the nth node from the end.
        
        We can use a dummy node to enable the .next.next minimum reassignment length
        when removing the node.

        time T(n) = O(n) -> scales with length of the linked list. "n" is not the shift as described above
        space S(n) = O(1) -> only storing the list no asymptote
        '''
        # if the sll is empty
        if head is None:
            return

        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next

# from typing import Optional

# class BruteForce:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         # if the linked list is empty return
#         if head is None:
#             return
        
#         # Traverse the linked list to find the length of the linked list
#         length = 0
#         current = head
#         while current is not None:
#             length += 1
#             current = current.next
        
#         # if the nth node from the end is the first node, remove it by setting the head to the next node
#         if n == length:
#             head = head.next
#             return head
        
#         # Otherwise traverse the linked list again to find the previous node of the nth node from the end
        
#         # e.g. length = 5, n = 2, iterate i up to length - n - 1 = 5 - 2 - 1 = 2
#         # i = 0; current = [1, LL[2, LL[3, LL[4, LL[5, None]]]]]
#         # i = 1; c urrent = LL[2, LL[3, LL[4, LL[5, None]]]]
#         # i = 2; current = LL[3, LL[4, LL[5, None]]]
#         # current node points to the previous node of the nth node from the end that we want to remove
        
#         current = head
#         i = 0
#         while i < length - n - 1:
#             current = current.next
#             i += 1       
        
#         # Set the next node of the current node to the node after the nth node from the end,
#         # effectively removing the nth node from the end 
#         current.next = current.next.next
#         return head


# @lc code=end

