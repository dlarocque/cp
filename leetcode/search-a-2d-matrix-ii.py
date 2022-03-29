class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row, col = m-1, 0
        
        while col < n and row >= 0:
            elem = matrix[row][col]
            
            if elem > target:
                row -= 1
            elif elem < target:
                col += 1
            else:
                return True
        
        return False
