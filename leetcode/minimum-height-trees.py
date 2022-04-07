class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Given an acyclic, nondirected graph, return a list of all MHT's root labels

        All of the possible first elements in a topological sorting of the tree

        """
        min_height, mht_roots = 0, []
        visited = [0] * n

        def dfs(k: int) -> bool:
            if visited[k] == -1:
                return False
            if visited[k] == 1:
                return True
            visited[k] = -1
            for 

            return True


        return mht_roots
        
