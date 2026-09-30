#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (77.34%)
# Likes:    12952
# Dislikes: 270
# Total Accepted:    2.4M
# Total Submissions: 3.1M
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# Given the root of a binary search tree, and an integer k, return the k^th
# smallest value (1-indexed) of all the values of the nodes in the tree.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is n.
# 1 <= k <= n <= 10^4
# 0 <= Node.val <= 10^4
# 
# 
# 
# Follow up: If the BST is modified often (i.e., we can do insert and delete
# operations) and you need to find the kth smallest frequently, how would you
# optimize?
# 
#

# @lc code=start
# Definition for a binary tree node.
from sqlite3 import Time


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        """
        Given the root of a binary search tree, and an integer k, 
        return the kth smallest value (1-indexed) of all the values 
        of the nodes in the tree.
        
        Algorithm:
            1. Perform an in-order traversal of the BST.
            2. Keep a counter to track the number of nodes visited.
            3. When the counter reaches k, return the current node's value.
        
        Args:
            root (TreeNode): The root of the binary search tree.
            k (int): The 1-indexed position of the smallest element to find.
        
        Returns:
            int: The kth smallest value in the BST.

        @complexity:    
            Time Complexity: T(n) = O(n) in the worst case, where n is the number of nodes in the tree.
            Space Complexity: S(n) = O(h) due to the recursion stack, where h is the height of the tree.
        """
        stack = []
        current = root
        count = 0
        
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            count += 1
            if count == k:
                return current.val
            current = current.right
        # If k is out of bounds, return None
        return None
        
# @lc code=end

