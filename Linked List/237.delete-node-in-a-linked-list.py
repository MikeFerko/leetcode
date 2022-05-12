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
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # [4,5,1,9] -> [4,1,9]
        # Not really deleting the node, but reassigning the node to
        #the next node's value and the next node's next pointer
        node.val = node.next.val
        node.next = node.next.next
        
# @lc code=end

