class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        spiral = []
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # R, D, L, U
        direction_idx = 0
        direction = directions[direction_idx]
        VISITED = 101

        x, y = 0, 0
        while x >= 0 and x < m and y >= 0 and y < n:
            spiral.append(matrix[x][y])
            matrix[x][y] = VISITED

            next_x = x + direction[0]
            next_y = y + direction[1]

            turns = 0
            while next_x >= m or next_y >= n or matrix[next_x][next_y] == VISITED:
                # we've tried turning in all directions
                if turns == 3:
                    return spiral

                # change diretions and try again
                direction_idx += 1
                direction_idx %= 4
                direction = directions[direction_idx]
                turns += 1
                next_x = x + direction[0]
                next_y = y + direction[1]

            x = next_x
            y = next_y
