class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """
        N = mn

        Time complexity: O(3^N), since we have three directions to visit for 
        each open cell
        Space complexity: O(N), recursion stack
        """
        m, n = len(grid), len(grid[0])
        res, total_empty = 0, 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or grid[i][j] == 1:
                    total_empty += 1
        
        def dfs(i: int, j: int, to_visit: int) -> None:
            nonlocal res
            if grid[i][j] == 2:
                if to_visit == 0: res += 1
                return
            elif grid[i][j] == -1 or (grid[i][j] == 1 and to_visit < total_empty):
                return
            
            for x,y in directions:
                new_i, new_j = i+x, j+y
                if 0 <= new_i < m and 0 <= new_j < n:
                    grid[i][j] = -1
                    dfs(new_i, new_j, to_visit-1)
                    grid[i][j] = 0
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j, total_empty)
                    return res
                
        return -1
