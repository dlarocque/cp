class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # search for the first char in word, do dfs
        self.directions = [[0,1], [-1, 0], [0, -1], [1, 0]]
        self.m, self.n = len(board), len(board[0])

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    if self.dfs(board, word[1:], [(i, j)], i, j):
                        return True

    def dfs(self, board, word, visited, i, j) -> bool:
        if not word:
            return True

        direction_idx = 0

        while direction_idx < 4:
            direction = self.directions[direction_idx]
            next_i = i + direction[0]
            next_j = j + direction[1]

            if next_i >= 0 and next_i < self.m and next_j >= 0 and next_j < self.n:
                if (next_i, next_j) not in visited and board[next_i][next_j] == word[0]:
                    if self.dfs(board, word[1:], visited+[(next_i, next_j)], next_i, next_j):
                        return True

            direction_idx += 1

        return False
