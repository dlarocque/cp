class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Solution:
        We can store what rows and cols need to be replaced with zeroes if we
        replace the first row and cols with a value of 0, and use that as a flag
        that we need to replace that row or column. 
        A problem that arises is that while replacing the first row and column
        we end up creating "false" flags by setting the first row and column 0's.
        So, we use rowZero and colZero to denote whether the first row and col
        need to replaced, then replace all the others normally without having
        to set false flags as we're replacing.
        """
        m, n, colZero, rowZero = len(matrix), len(matrix[0]), False, False
        
        # first row
        for j in range(n):
            if matrix[0][j] == 0:
                rowZero = True
        
        # first col
        for i in range(m):
            if matrix[i][0] == 0:
                colZero = True
        
        # all but first row and col
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        # replace all but first row and col
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # replace first row
        if rowZero:
            for j in range(n):
                matrix[0][j] = 0
        
        # replace first col
        if colZero:
            for i in range(m):
                matrix[i][0] = 0
                    
                    
