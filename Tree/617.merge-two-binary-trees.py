#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        root1 : input binary tree 1
        root2 : input binary tree 2
        mergedTree : output merged trees of binery tree 1 and tree 2

        Algorithm: Tranverse the two trees using recursive depth first search in preorder
        as is the ordering of the input trees and check if the node exists. If the node exists
        add the value and assign that value to that node. Search the left child all the way.
        Search the right child as we work our way up from the depth of the branches. At each node
        we still check if the value exists, the left child exists and then the right child exists
        as is required of preorder dfs traversal.

        time T(n) = O(n + m) -> where n is the height of tree 1 and m is the height of tree 2
        space S(n) = O(n + m) -> worst case store both trees and both trees have long single branches
        '''
        
        # base case if the trees are empty then we merge nothing
        if not root1 and not root2:
            return  None

        # preorder traversal as input is given in preorder.
        # start with root
        if root1:
            val1 = root1.val
        else:
            val1 = 0
        
        if root2:
            val2 = root2.val
        else:
            val2 = 0
        mergedTree = TreeNode(val1 + val2)

        # next in preorder binary tree traversal is left child
        if root1:
            left1 = root1.left
        else:
            left1 = None
        if root2:
            left2 = root2.left
        else:
            left2 = None
        mergedTree.left = self.mergeTrees(left1, left2)

        # lastly in preorder binary tree traversal we have the right child
        if root1:
            right1 = root1.right
        else:
            right1 = None
        if root2:
            right2 = root2.right
        else:
            right2 = None
        mergedTree.right = self.mergeTrees(right1, right2)

        return mergedTree



# @lc code=end

