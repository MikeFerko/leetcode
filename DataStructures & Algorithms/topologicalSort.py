'''
Topological Sort (Kahn's Algorithm, BFS-based)

Orders the nodes of a directed acyclic graph (DAG) so that every edge
u -> v places u before v in the result -- i.e. a valid order to do
"tasks with prerequisites" in. Works by repeatedly peeling off nodes
that currently have no remaining incoming edges (in-degree 0).

If the graph has a cycle, some nodes will never reach in-degree 0, and
the result will end up shorter than the total node count -- that's how
this doubles as cycle detection (see Course Schedule, LC 207).

Time Complexity: T(n) = O(|V| + |E|)
Space Complexity: S(n) = O(|V| + |E|), for the adjacency list and in-degree array
'''

from collections import defaultdict, deque

class Graph:
    def __init__(self, numNodes: int):
        self.numNodes = numNodes
        self.graph = defaultdict(list)
        self.inDegree = [0] * numNodes

    def addEdge(self, u: int, v: int) -> None:
        # u must come before v
        self.graph[u].append(v)
        self.inDegree[v] += 1

    def topologicalSort(self):
        # start with every node that has no prerequisites left
        queue = deque([node for node in range(self.numNodes) if self.inDegree[node] == 0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            # "remove" this node from the graph by decrementing its
            # neighbors' in-degree -- any neighbor that drops to 0 now
            # has all of its prerequisites satisfied
            for neighbor in self.graph[node]:
                self.inDegree[neighbor] -= 1
                if self.inDegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != self.numNodes:
            # some nodes never hit in-degree 0 -- a cycle is holding them back
            return None
        return order


# Driver code
if __name__ == "__main__":
    # 0 -> 1 -> 3
    #      1 -> 2
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(1, 3)

    print(f"Topological order: {g.topologicalSort()}")  # e.g. [0, 1, 2, 3]

    # introduce a cycle: 2 -> 0 means 0 now depends on something after it
    gCyclic = Graph(3)
    gCyclic.addEdge(0, 1)
    gCyclic.addEdge(1, 2)
    gCyclic.addEdge(2, 0)

    print(f"Cyclic graph result: {gCyclic.topologicalSort()}")  # None -- cycle detected
