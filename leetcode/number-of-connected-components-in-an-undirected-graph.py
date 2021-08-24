class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        edges = [[0,1],[1,2],[3,4]]
        adj_list = [[1],[0,2],[1],[4],[3]]
        visited = [0: True, 1:True, 2:True, ]
        num_components = 1
        """
        visited = {}
        num_components = 0

        adj_list = [[] for _ in range(n)]
        # construct an adjacency list
        for v, w in edges:
            adj_list[v].append(w)
            adj_list[w].append(v)

        def dfs(v: int) -> None:
            if v in visited:
                return

            visited[v] = True
            for w in adj_list[v]:
                dfs(w)

        for v in range(n):
            if v not in visited:
                num_components += 1
                dfs(v)

        return num_components
