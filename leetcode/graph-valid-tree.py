class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        A tree is a graph containing undirected edges with no cycles

        1. Generate a list of edges connected to each node
        2. Perform a DFS on each node in the tree to see if that search
        reaches the same node twice, if it does, we know there exists a cycle
        """
        m = len(edges)

        graph = [[] for _ in range(n)]

        for x, y in edges:
            graph[y].append(x)
            graph[x].append(y)

        for i in range(n):
            visited_vertices = [0] * n
            visited_edges = [[] for _ in range(n)]
            if not self.dfs(graph, visited_vertices, visited_edges, i):
                return False

            if 0 in visited_vertices:
                return False

        return True


    def dfs(self, graph, visited_vertices, visited_edges, i) -> bool:
        # we visited the same vertex twice without visiting the same edge twice
        # so there must be a cycle in the tree
        if visited_vertices[i] == 1:
            return False

        visited_vertices[i] = 1

        for j in graph[i]:
            if j not in visited_edges[i] and i not in visited_edges[j]:
                visited_edges[i].append(j)
                visited_edges[j].append(i)
                if not self.dfs(graph, visited_vertices, visited_edges, j):
                    return False

        return True
