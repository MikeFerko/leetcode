'''
Depth-First Search (DFS)

Time complexity: T(n) = O(|V| + |E|), where V is the number of vertices and E is the number of edges in the graph.
Space Complexity: S(n) = O(|V|), since an extra visited array of size V is required.

|V| = magnitude i.e. number of Vertices/Nodes
|E| = magnitude i.e. number of Edges/Relationships
'''

from collections import defaultdict

class Graph:
    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u:int, v:int):
        self.graph[u].append(v)
    
    # A function used by DFS
    def DFSUtil(self, v:int, visited:set):

        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')

        # recurse for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # The function to do the DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v:int):
        print(type(v))

        # Create a set to store visited vertices
        visited = set()

        # Call the recusive helper function
        # to print DFS traversal ndoes
        self.DFSUtil(v, visited)

# Driver code
if __name__ == "__main__":
    # Create a graph given in
    # the above diagram
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print(f"DFS Traversal of adjacency list: {g.graph}")
    g.DFS(2)
    print("\n")

