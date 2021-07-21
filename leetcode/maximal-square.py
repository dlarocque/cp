class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_size = 0
        rows, cols = len(matrix), len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if int(matrix[row][col]) == 1:
                    if row == 0 or col == 0:
                        max_size = max(1, max_size)
                    else:
                        size = min(int(matrix[row-1][col]), int(matrix[row-1][col-1]), int(matrix[row][col-1])) + 1
                        matrix[row][col] = str(size)
                        max_size = max(max_size, size)
        return pow(max_size, 2)
