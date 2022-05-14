class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Return weight of path from node k to all nodes
        Spanning tree algorithm
        
        max path from k to all nodes
        """
        
        # create an adjacency list
        graph = [[] for _ in range(n+1)]
        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = [0]+[math.inf]*n
        dist[k] = 0
        # bellman-fjord algorithm (shortest path)
        for _ in range(n):
            for u, v, w in times:
                dist[v] = min(dist[v], dist[u]+w)
                
        for d in dist:
            if d == math.inf:
                return -1
            
        return max(dist)
        
        
        
