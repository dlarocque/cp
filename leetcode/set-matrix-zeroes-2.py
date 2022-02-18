class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Solution 1: 
        Brute-force replace a row and column with 0's when we find one
        Time: O(nm^2) in the case where we already have all 0's
        Space: O(1)
        
        Solution 2: 
        Iterate through the entire matrix, storing the row and column
        numbers when we find a 0, then replacing those rows and columns with 0's
        Time: O(nm)
        Space: O(mn)
        """
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        
        # first-pass
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
                    
        for row in rows:
            for j in range(n):
                matrix[row][j] = 0
        
        for col in cols:
            for i in range(m):
                matrix[i][col] = 0
                    
                    
