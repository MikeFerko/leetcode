'''
Union-Find (Disjoint Set Union / DSU)

Tracks a collection of elements split into disjoint groups, and answers
"are these two elements in the same group?" and "merge these two groups"
efficiently. Backed by path compression (find flattens the tree as it
walks up) and union by rank (always attach the shorter tree under the
taller one), which together keep both operations nearly O(1).

Time Complexity: T(n) = O(alpha(n)) per find/union, where alpha is the
inverse Ackermann function -- effectively constant for any n that fits
in memory.
Space Complexity: S(n) = O(n) for the parent/rank arrays.

Classic use cases: detecting cycles in an undirected graph, counting
connected components, Kruskal's MST.
'''

class UnionFind:
    def __init__(self, n: int):
        # each node starts as its own parent (its own group of one)
        self.parent = list(range(n))
        # rank is a rough upper bound on tree height, used to keep unions balanced
        self.rank = [0] * n
        self.count = n  # number of disjoint groups remaining

    def find(self, x: int) -> int:
        # walk up to the root of x's group
        if self.parent[x] != x:
            # path compression: point x directly at the root on the way back out,
            # so future find() calls on x (and anything under it) are O(1)
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            # already in the same group -- this is the "cycle detected" case
            # when union-find is used for cycle detection on an undirected graph
            return False

        # union by rank: attach the shorter tree under the taller one
        if self.rank[rootX] < self.rank[rootY]:
            rootX, rootY = rootY, rootX
        self.parent[rootY] = rootX
        if self.rank[rootX] == self.rank[rootY]:
            self.rank[rootX] += 1

        self.count -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


# Driver code
if __name__ == "__main__":
    # 5 nodes, initially 5 separate groups
    uf = UnionFind(5)

    print(f"Initial groups: {uf.count}")  # 5

    uf.union(0, 1)
    uf.union(1, 2)
    print(f"After union(0,1) and union(1,2): {uf.count} groups")  # 3
    print(f"connected(0, 2): {uf.connected(0, 2)}")  # True (0-1-2 merged)
    print(f"connected(0, 3): {uf.connected(0, 3)}")  # False

    # unioning two already-connected nodes signals a cycle
    madeProgress = uf.union(0, 2)
    print(f"union(0, 2) again -- new merge? {madeProgress}")  # False, cycle
