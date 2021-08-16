class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = [] # rows that have a 0
        zero_cols = [] # cols that have a 0

        for row_num, row in enumerate(m):
            for col_num, col in enumerate(row):
                if m[row_num][col_num] == 0:
                    if row_num not in zero_rows: zero_rows.append(row_num)
                    if col_num not in zero_cols: zero_cols.append(col_num)

        # clear the rows and cols with zeroes
        for row in zero_rows:
            for col in range(len(m[row])):
                m[row][col] = 0

        for col in zero_cols:
            for row in range(len(m)):
                m[row][col] = 0

