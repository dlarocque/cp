class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        num_closed_islands = 0
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        
        def dfs_expand(row: int, col: int, val: int) -> None:
            nonlocal grid, m, n, directions
            if grid[row][col] == val:
                return
            
            grid[row][col] = val
            for x, y in directions:
                new_row, new_col = row+x, col+y
                if 0 <= new_row < m and 0 <= new_col < n:
                    dfs_expand(new_row, new_col, val)
                    
        # expand water from edges to islands
        for row in range(m):
            dfs_expand(row, 0, 1)
            dfs_expand(row, n-1, 1)
        
        for col in range(n):
            dfs_expand(0, col, 1)
            dfs_expand(m-1, col, 1)
            
        # find remaining water within the islands
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    num_closed_islands += 1
                    dfs_expand(row, col, 1)
                    
        return num_closed_islands
