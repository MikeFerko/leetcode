#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from typing import Optional

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        '''
        root : input perfect binary tree
        root : output Linked List between levels in the perfect binary tree
        
        Algorithm: perform bfs on the tree and use each case to solve the next within the level.
        Using the fact that this is a perfect binary tree means that there will always be two children nodes
        at each level and all the leaf nodes are situated at the same level in the tree. This means
        that our loop terminationa condition can be when there is no current node and no next node.
        We can use the parent node as our current node and the next node to look at will be the left child.
        We take the parent node left child and assign the next pointer to the right child of that parent node.
        If there is a next pointer at out level then we take the right child of the current node
        jump to the next pointer we made and assign the right child's next pointer to the parent node's 
        left child. This bridges the connection from the left to the right subtree.
        
        We then move over to that next node of our parent node and set that to our current node and perform the
        same operations in our loop.
        
        When the currentNode is null we will have reached the end of the level
        and need to assign the parent node to the next node variable and set the next node variable to the
        parent node's left child.
        
        Meaning that we aiterate level by level making our linked list next connections at each level
        as we traverse the perfect binary tree.
        
        time T(n) =  O(n) -> traverse the entire tree.
        space S(n) = O(1) -> no extra storage'''

        # perform bfs and connect the nodes at each level.
        currentNode = root
        if root:
            nextNode = currentNode.left
        else:
            nextNode = None
        
        while currentNode and nextNode:
            currentNode.left.next = currentNode.right
            if currentNode.next:
                currentNode.right.next = currentNode.next.left
            
            currentNode = currentNode.next
            if not currentNode:
                currentNode = nextNode
                nextNode = currentNode.left
        return root

# @lc code=end

