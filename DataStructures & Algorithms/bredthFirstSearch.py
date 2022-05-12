'''
Depth-First Search (DFS)

Time complexity: T(n) = O(|V| + |E|), where V is the number of vertices and E is the number of edges in the graph.
Space Complexity: S(n) = O(|V|)

|V| = magnitude i.e. number of Vertices/Nodes
|E| = magnitude i.e. number of Edges/Relationships
'''

from collections import defaultdict
# A default dictionary is a dictionary that 
# automatically assigns defpault values to keys, 
# if queried keys are not present.

class Graph:
    # constructor
    def __init__(self):

        # default dictionary to store a graph
        self.graph = defaultdict(list)
    
    # function to add an edge to a graph
    def addEdge(self, u:int, v:int):
        self.graph[u].append(v)

    # function to return a BFS of a source node from a graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # create a queue fro the BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue
            s = queue.pop(0)
            print (s, end = " ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If an adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

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

    print(f"BFS Traversal of adjacency list: {g.graph}")
    g.BFS(2)
    print("\n")