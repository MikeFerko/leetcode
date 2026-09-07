#
# @lc app=leetcode id=237 lang=python3
#
# [237] Delete Node in a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''
LeetCode solution 
'''
class Solution:
    def deleteNode(self, node):
        """
        Given a node (not the tail) in a singly-linked list, delete it
        in-place without access to the head. Since the node itself can't be
        unlinked, its value and next pointer are overwritten with those of
        the following node, effectively deleting the next node instead.

        Args:
            node (ListNode): the node to delete, guaranteed not the tail

        Returns:
            None: modifies the list in-place instead

        @complexity: Time: O(1)
        @complexity: Space: O(1)
        """
        # [4,5,1,9] -> [4,1,9]
        # Not really deleting the node, but reassigning the node to
        #the next node's value and the next node's next pointer
        node.val = node.next.val
        node.next = node.next.next
        
# @lc code=end

