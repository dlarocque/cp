class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        """
        place n-queens on an nxn chess board
        
        """
        res = 0
        column, left_diagonal, right_diagonal = [False]*n, [False]*(2*n-1), [False]*(2*n-1)
        board = ['.'*n for _ in range(n)]
        
        def dfs(y: int, board: List[List[str]]) -> None:
            nonlocal res, n, column, left_diagonal, right_diagonal
            if y == n:
                res += 1
                return
            
            for x in range(n):
                if column[x] or left_diagonal[x+y] or right_diagonal[x-y+n-1]:
                    continue
                column[x] = left_diagonal[x+y] = right_diagonal[x-y+n-1] = True
                dfs(y+1, board)
                column[x] = left_diagonal[x+y] = right_diagonal[x-y+n-1] = False
                
        
        dfs(0, board)
        return res
