#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.

'''
traverse tree in level order meaning left to right, top to bottom.
This traversal by level order is just Bredth Frist Search (BFS)

We can use a queue to add elements at end of queue and pop elements by first in first out (FIFO)

We add values to the queue when disccovering node values at each level

"""

root = [3,9,20,null,null,15,7]

Constructed BST is

3
/ \
9 20
/ \ / \
x x 15 7
"""

S(n) = O(|V|) -> O(n)
T(n) = O(|E| + |V|)
'''
from typing import Optional, List
import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelOrder = []

        q = collections.deque()
        q.append(root)
        
        while q:
            qLen = len(q)
            level = [] # initialize at each level of the BST
            for v in range(0, qLen): # v for vertice
                # if we pop the first element every time we get the next vertex
                # in the binary tree breadth i.e. width first search which we could use for
                # measuring distances between source and target nodes.
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                # add the node value level list to level order 2x2 matrix every time we finish with w level deque
                levelOrder.append(level) 
        return levelOrder

# @lc code=end

