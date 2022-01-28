class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def dfs(word: str, row: int, col: int, visited: set) -> bool:
            if (row, col) in visited:
                return False
            
            # base case
            if not word:
                return True
            
            for d in dirs:
                next_row, next_col = row+d[0], col+d[1]
                if 0 <= next_row < m and 0 <= next_col < n:
                    if board[next_row][next_col] == word[0]:
                        if dfs(word[1:], next_row, next_col, visited|{(row,col)}):
                            return True
                        
            # went in all direction and didn't find the word
            return False
        
        for row in range(m):
            for col in range(n):
                visited = set()
                if word[0] == board[row][col] and dfs(word[1:], row, col, visited):
                    return True
                
        return False
