class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        // find an island '1'
        // increase the number of islands
        // 'down' the island by turning all adjacent
        // lands into 0's
        int maxArea = 0;
        for(int x = 0; x < grid.length; x++) {
            for(int y = 0; y < grid[x].length; y++) {
                if(grid[x][y] == 1) {
                    maxArea = Math.max(maxArea, sink(grid, x, y));
                }
            }
        }
        
        return maxArea;
    }
    
    public int sink(int[][] grid, int x, int y) {
        if(x < 0 || x == grid.length || y < 0 || y == grid[0].length || grid[x][y] == 0)
            return 0;
        grid[x][y] = 0;
        int area = 1;
        area += sink(grid, x-1, y);
        area += sink(grid, x+1, y);
        area += sink(grid, x, y-1);
        area += sink(grid, x, y+1);
        return area;
    }
}
