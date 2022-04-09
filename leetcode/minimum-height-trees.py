class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Find the nodes in the middle of the two furthest nodes in the graph

        We can find the furthest nodes by doing two DFS' O(n)
        Find the middle nodes by travelling diameter//2 edges from one of the furthest nodes

        There are two possible roots if diameter is odd
        One possible root if diameter is even
        """
        if len(edges) < 2:
            return [i for i in range(n)]
        graph, in_degree = [set() for _ in range(n)], []

        # Create adjacency list
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = [i for i in range(n) if len(graph[i]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                parent = graph[leaf].pop()
                graph[parent].remove(leaf)
                if len(graph[parent]) == 1:
                    new_leaves.append(parent)

            leaves = new_leaves

        return leaves


        


        
