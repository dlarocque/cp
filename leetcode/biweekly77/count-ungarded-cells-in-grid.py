class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        """
        create a mxn grid
        
        cnt = m*n
        for all x,y of guards
            cnt -= 1 
            guarded = true
            for all directions
                if pos is a wall
                    guarded = false
                pos = guarded
                
        """
        cnt = 0
        
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        grid = [[0 for _ in range(n)] for _ in range(m)]
        
        for wall_x, wall_y in walls+guards:
            grid[wall_x][wall_y] = 1
        
        for row, col in guards:
            for x, y in directions:
                trow, tcol = row+x, col+y

                while 0<=trow<m and 0<=tcol<n:
                    if grid[trow][tcol] == 1: # wall or another guard
                        break
                    grid[trow][tcol] = -1
                    trow += x
                    tcol += y
                            
        for row in grid:
            for cell in row:
                if cell == 0:
                    cnt += 1
           
        return cnt
