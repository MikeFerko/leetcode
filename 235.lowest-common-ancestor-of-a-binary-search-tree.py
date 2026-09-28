#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#
# algorithms
# Medium (71.39%)
# Likes:    12506
# Dislikes: 367
# Total Accepted:    2.4M
# Total Submissions: 3.4M
# Testcase Example:  '[6,2,8,0,4,7,9,null,null,3,5]\n2\n8'
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node
# of two given nodes in the BST.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of
# itself).”
# 
# 
# Example 1:
# 
# 
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# 
# 
# Example 2:
# 
# 
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant
# of itself according to the LCA definition.
# 
# 
# Example 3:
# 
# 
# Input: root = [2,1], p = 2, q = 1
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q will exist in the BST.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Given a binary search tree (BST) and two nodes p and q, return their lowest common ancestor (LCA).
        
        According to the definition of LCA on Wikipedia: “The lowest common ancestor
        is defined between two nodes p and q as the lowest node in T that has both p
        and q as descendants (where we allow a node to be a descendant of
        itself).”
        
        Algorithm:
            1. Start from the root of the BST.
            2. If both p and q have values smaller than the current node, move to the left child.
            3. If both p and q have values larger than the current node, move to the right child.
            4. If p and q lie on opposite sides of the current node, the current node is the LCA.
        
        Args:
            root (TreeNode): The root of the BST.
            p (TreeNode): The first node.
            q (TreeNode): The second node.

        Returns:
            TreeNode: The lowest common ancestor of nodes p and q.
        
        @complexity:
            Time: T(h) = O(h), where h is the height of the BST.
            Space: S(h) = O(1) for the iterative approach.
            Note: The recursive approach would have a space complexity of O(h) due to the call stack.
        """
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
        return None
# @lc code=end

