class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range (n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        res += 1
                    else:
                        sq = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]) + 1
                        res += sq
                        matrix[i][j] = sq
        return res
