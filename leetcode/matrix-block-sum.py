class Solution:
    def matrixBlockSum(self, matrix: List[List[int]], k: int) -> List[List[int]]:
        """Prefix sum

        O(mn) time
        O(mn) space
        """

        # Compute the Prefix sum matrix
        prefix = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        for i in range(1, len(prefix)):
            summation = 0
            for j in range(1, len(prefix[0])):
                summation += matrix[i-1][j-1]

                prefix[i][j] = summation + prefix[i-1][j]

        # Compute the answers for each element
        res = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                min_row, max_row = max(0, i-k-1), min(len(matrix), i+k)
                min_col, max_col = max(0, j-k-1), min(len(matrix[0]), j+k)

                res[i-1][j-1] = prefix[max_row][max_col] - prefix[max_row][min_col] - prefix[min_row][max_col] + prefix[min_row][min_col]

        return res
