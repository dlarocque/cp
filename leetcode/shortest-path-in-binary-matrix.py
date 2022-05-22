class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        shortest path from (0, 0) to (n-1, n-1)

        BFS Solution:
        Store visited cells in a dictionary, don't revisit cells
        Initialize queue of cells to visit with (0,0)
        while queue is not empty
            for all cells in queue
                if cell == (n-1, n-1)
                    return steps taken to cell

                for all directions
                    if cell+direction has not been visited
                        add cell+direction to queue with steps+1


        return -1

        Notes:
        - Can move in all directions (including diagonals)
        - It takes fewer steps to go diagonally if possible
        """
        n = len(grid)
        if n == 1:
            return 1 if grid[0][0] == 0 else -1
        if grid[0][0] == 1:
            return -1
        directions = [[1,0], [1,1], [0,1], [-1, 1], [-1,0], [0,-1], [-1,-1], [1, -1]]
        queue = [(0,0,1)] # (row, col, steps)
        visited = {} # (row, col)
        visited[(0,0)] = True
        
        while queue:
            next_queue = []
            for row, col, steps in queue:
                for x, y in directions:
                    new_row, new_col = row+x, col+y
                    if 0 <= new_row < n and 0 <= new_col < n:
                        if grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                            if new_row == n-1 and new_col == n-1:
                                return steps+1

                            visited[(new_row, new_col)] = True
                            next_queue.append((new_row, new_col, steps+1))

            queue = next_queue

        return -1 
