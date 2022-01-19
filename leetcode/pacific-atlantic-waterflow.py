class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        
        # land that touches each of the oceans
        pacific_land, atlantic_land = set(), set()
        m, n = len(matrix), len(matrix[0])
        
        def spread(i, j, land):
            """ Expand matrix[i][j] as far as possible"""
            land.add((i, j))
            for x, y in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
                if (0 <= x < m and 0 <= y< n and matrix[x][y] >= matrix[i][j]
                        and (x, y) not in land):
                    spread(x, y, land)

        for i in range(m):
            spread(i, 0, pacific_land)
            spread(i, n-1, atlantic_land)
            
        for j in range(n):
            spread(0, j, pacific_land)
            spread(m-1, j, atlantic_land)
            
        return list(pacific_land & atlantic_land)
