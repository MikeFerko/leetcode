#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        let's try this iteratively first and then try recursion.

        head : input of linked list head node
        current : points to our current node
        previous : points to the previous node 
        next : points to our next node

        Algorithm: use pointer current to point to our current node
        and iterate through the linked list while current is not null.
        Store the next pointer of our current node in a temporary variable called next.
        set the next pointer of our current node to the previous node (at start will just point to null).
        Set the previous pointer to our current node. And update the current node to the temp
        variable next pointer. Once the loop terminates the new head of the lined list will be
        our preious node when current pointed to null. So we return previous as the head 
        of our reversed singly linked list.

        time T(n) = O(n) -> time proportional to the time it takes to iterate through the entire length of the input linked list
        space S(n) = O(1) -> just store constants each time no matter what.

        '''

        previous = None
        current = head
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        # now our previous is the head of the reversed linked list
        return previous

        '''
        Now let's try recursive.

        Algorithm: Iterate down to recursion tree tail until the end of the linked list.
        At the tail we will have split the entire linked list into subproblems. The tail
        will be our newHead pointing to null. upon traversal back up the recursion tree 
        our head will be at the preious node. So we want the next of the newHead node to point to our current head
        in the recursion tree upward traversal. but the head's next is already pointing to our reversed
        leaf branch which points to null. So we take the current head.next.next to point to our recursed head.
        and get the recursed head to point to null. Then return that subproblem up another hop 
        in our recursion tree as the newHead for head.next. So we have recursively reversed our link 
        at the tail of our linked list.

        In this method our recursion tree is bounded by the length of the original linked list to go down and then back up
        when the recursion tree ends at head we will have newHead pointing to the head of the reversed linked list
        and just return to the original function call in our computer's call stack.

        time T(n) = O(n) -> upper/lower bounded by total length of linked list
        space S(n) = O(n) -> we will always store entire length of linked list in newHead 
        when we reach the end of the recurssion calls.

        Since jwe have to go to the end of the linked list before we traverse back up our recursion tree
        - In this way it seems more efficient to perform an iterative method rather than recursive.
        '''
        # # base case linked list is empty
        # if not head:
        #     return None
        
        # newHead = head
        # if head.next:
        #     newHead = self.reverseList(head.next)
        #     head.next.next = head
        # head.next = None

        # return newHead

        

# @lc code=end

