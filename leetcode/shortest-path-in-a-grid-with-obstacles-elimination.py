import math
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        Notes
        - Can move up, down, left, right
        - Can not pass through obstacles (1's)
        - Can pass through at most k obstacles
        - Return minimum number of steps to go from (0,0) to (m-1, n-1)

        DFS, Backtracking, possible optimizations with re-visiting dead-ends

        [
                [0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,0],
                [0,1,0,0,0,0,0,0,0,0],
                [0,1,0,1,1,1,1,1,1,1],
                [0,1,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,0],
                [0,1,0,0,0,0,0,0,0,0],
                [0,1,0,1,1,1,1,1,1,1],
                [0,1,0,1,1,1,1,0,0,0],
                [0,1,0,0,0,0,0,0,1,0],
                [0,1,1,1,1,1,1,0,1,0],
                [0,0,0,0,0,0,0,0,1,0]]
                1

        """
        m, n = len(grid), len(grid[0])
        min_steps = m*n 
        directions = [[0,1], [1, 0], [0, -1], [-1, 0]]
        visited = set()

        queue = [(0, 0, k)]
        while queue:
            x, y, rem = queue.pop(0)

            if x == m-1 and y == n-1:

            visited.add((x,y,rem))
            for i, j in directions:
                if 0 <= x+i < m and 0 <= y+j < n:
                        if grid[x+i][y+j] == 1:
                            if (x, y, rem-1) not in visited:
                                queue.append((x+i, y+j, rem-1))
                        else:
                            if (x, y, rem) not in visited:
                                queue.append((x+i, y+j, rem))


        return min_steps if min_steps < m*n else -1
        
