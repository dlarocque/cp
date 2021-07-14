class Solution {
    public int numIslands(char[][] grid) {
        // find an island '1'
        // increase the number of islands
        // 'down' the island by turning all adjacent
        // lands into 0's
        int numIslands = 0;
        for(int x = 0; x < grid.length; x++) {
            for(int y = 0; y < grid[x].length; y++) {
                if(grid[x][y] == '1') {
                    numIslands++;
                    sink(grid, x, y);
                }
            }
        }
        
        return numIslands;
    }
    
    public void sink(char[][] grid, int x, int y) {
        if(x < 0 || x == grid.length || y < 0 || y == grid[0].length || grid[x][y] == '0')
            return;
        grid[x][y] = '0';
        sink(grid, x-1, y);
        sink(grid, x+1, y);
        sink(grid, x, y-1);
        sink(grid, x, y+1);
    }
}
