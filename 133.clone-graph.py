#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#
# https://leetcode.com/problems/clone-graph/description/
#
# algorithms
# Medium (65.23%)
# Likes:    10786
# Dislikes: 4229
# Total Accepted:    2M
# Total Submissions: 3.1M
# Testcase Example:  '[[2,4],[1,3],[2,4],[1,3]]'
#
# Given a reference of a node in a connected undirected graph.
# 
# Return a deep copy (clone) of the graph.
# 
# Each node in the graph contains a value (int) and a list (List[Node]) of its
# neighbors.
# 
# 
# class Node {
# ⁠   public int val;
# ⁠   public List<Node> neighbors;
# }
# 
# 
# 
# 
# Test case format:
# 
# For simplicity, each node's value is the same as the node's index
# (1-indexed). For example, the first node with val == 1, the second node with
# val == 2, and so on. The graph is represented in the test case using an
# adjacency list.
# 
# An adjacency list is a collection of unordered lists used to represent a
# finite graph. Each list describes the set of neighbors of a node in the
# graph.
# 
# The given node will always be the first node with val = 1. You must return
# the copy of the given node as a reference to the cloned graph.
# 
# 
# Example 1:
# 
# 
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val =
# 3).
# 
# 
# Example 2:
# 
# 
# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists
# of only one node with val = 1 and it does not have any neighbors.
# 
# 
# Example 3:
# 
# 
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the graph is in the range [0, 100].
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# There are no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given
# node.
# 
# 
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        """
        Initialize a Node with a value and a list of neighbors.
        
        Args:
            val (int): The value of the node.
            neighbors (List[Node], optional): A list of neighboring nodes. Defaults to None.
        """
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Clone a connected undirected graph.

        Algorithm:
            1. Use a depth-first search (DFS) approach to traverse the graph.
            2. Maintain a dictionary to map original nodes to their cloned counterparts.
            3. For each node, create a new node with the same value and recursively clone its neighbors.
            4. Return the cloned node corresponding to the input node.
        
        Args:
            node (Node): The reference node of the graph to be cloned.
        
        Returns:
            Node: The reference node of the cloned graph.
        
        @complexity:
            Time Complexity: T(N, E) = O(N + E), where N is the number of nodes and E is the number of edges in the graph.
            Space Complexity: S(N) = O(N), for storing the cloned nodes in the dictionary.
        """
        if not node:
            return None
        
        # A dictionary to keep track of current nodes that have already been cloned.
        cloned_nodes = {}
        
        def dfs(current_node: 'Node') -> 'Node':
            """
            Perform a depth-first search to clone the graph.
            
            Args:
                current_node (Node): The current node being visited.
            
            Returns:
                Node: The cloned node corresponding to the current node.
            
            @complexity:
                Time Complexity: T(N, E) = O(N + E), where N is the number of nodes and E is the number of edges in the graph.
                Space Complexity: S(N) = O(N), for storing the cloned nodes in the dictionary
            """
            # If the node has already been cloned, return the cloned node
            if current_node in cloned_nodes:
                return cloned_nodes[current_node]
            
            # Create a new node with the same value
            cloned_node = Node(current_node.val)
            cloned_nodes[current_node] = cloned_node
            
            # Recursively clone all neighbors
            for neighbor in current_node.neighbors:
                cloned_node.neighbors.append(dfs(neighbor))
            
            return cloned_node
        
        return dfs(node)

# @lc code=end

