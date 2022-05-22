class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        6
        [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]

        [[1, 2], [0, 2, 3], [1, 0], [1, 4, 5], [3, 5], [4, 3]]

        vital connection:
        x -> y
        x -> y -> z (two vital connections, despite length of adj list for y being len 2)

        serious graph theory bro

        Idea 1: check lenght of adj list (incorrect)

        No more ideas :( graph theory too hard bro

        Tarjan's algorithm:
        """
        critical_connections = []

        # create adjacency list
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            
        #print(graph)
        for u in range(n):
            if len(graph[u]) == 1:
                critical_connections.append([u, graph[u][0]])
                if len(graph[graph[u][0]]) == 1:
                    graph[graph[u][0]] = []
                
                graph[u] = []
        
        return critical_connections
