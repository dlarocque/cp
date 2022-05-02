class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        Graph Theory
        Graph is bipartite if it is acyclic, or its cycles are of even length.

        When we find a cycle, do another search to find how long the cycle is

        Find the length of a cycle
        Find the length of all cycles
        """
        n = len(graph)
        visited = [0]*n

        def cycle_len(node: int):
            return 0

        def dfs(node: int, prev: int, path_len: int):
            nonlocal graph, visited
            # cycle detection
            if visited[node] == -1:
                cycle_len(node)
                return path_len % 2 != 0
            elif visited[node] == 1:
                return True
            
            visited[node] = -1
            for adj in graph[node]:
                if adj != prev and not dfs(adj, node, path_len+1):
                    return False

            visited[node] = 1
            return True

        for node in graph:
            for adj in node:
                if not dfs(adj, -1, 0):
                    return False

        return True
