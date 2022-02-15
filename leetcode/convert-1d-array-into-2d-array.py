class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        
        new = [[0 for _ in range(n)] for _ in range(m)]
        
        for row in range(m):
            for col in range(n):
                new[row][col] = original[(row*n)+col]
                
        return new
