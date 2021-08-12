class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # flip the image
        for i in range(n//2):
            temp_row = matrix[i]
            matrix[i] = matrix[n-1-i]
            matrix[n-1-i] = temp_row

        # reverse the symmetry of the image
        for row in range(n):
            for col in range(row, n):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
