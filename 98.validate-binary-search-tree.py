#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (36.37%)
# Likes:    18682
# Dislikes: 1468
# Total Accepted:    3.6M
# Total Submissions: 9.8M
# Testcase Example:  '[2,1,3]'
#
# Given the root of a binary tree, determine if it is a valid binary search
# tree (BST).
# 
# A valid BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys strictly less than
# the node's key.
# The right subtree of a node contains only nodes with keys strictly greater
# than the node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [2,1,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        """
        Given the 'root' of a binary tree, determine if it is a valid binary search tree (BST).
        
        Algorithm:
            1. Perform an in-order traversal of the tree.
            2. During the traversal, check if the current node's value is greater than the previous node's value.
            3. If any node violates this property, the tree is not a valid BST.
            4. If all nodes satisfy the property, the tree is a valid BST.

        Args:
            root (TreeNode): The root of the binary tree.

        Returns:
            bool: True if the tree is a valid BST, False otherwise.
        
        @complexity:
            Time: T(n) = O(n), where n is the number of nodes in the tree.
            Space: S(h) = O(h), where h is the height of the tree due to the recursion stack.
        """

        # Helper function to perform in-order traversal and validate BST property.
        def inorder(node, prev):
            if not node:
                return True, prev
            is_valid, prev = inorder(node.left, prev)
            if not is_valid:
                return False, prev
            if prev is not None and node.val <= prev:
                return False, prev
            prev = node.val
            return inorder(node.right, prev)

        is_valid, _ = inorder(root, None)
        return is_valid
        
# @lc code=end

