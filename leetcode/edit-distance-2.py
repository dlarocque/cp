class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        distance(a,b) = distance from word1[:a] to word2[:b]
        distance(a,b) = min(distance(a,b-1)+1,
                            distance(a-1,b)+1,
                            distance(a-1,b-1)+cost(a,b))
        cost(a,b) = 0 if word1[a] == word2[b] else 1
        
        Insert:  distance(a, b-1)+1
        Delete:  distance(a-1, b)+1
        Replace: distance(a-1, b-1) + 1
        Match:   distance(a-1, b-1) + 0
        """
        if not word1: return len(word2)
        if not word2: return len(word1)
        
        memo = [[-1 for _ in range(len(word2))] for _ in range(len(word1))]
        
        def cost(a: int, b: int) -> int:
            nonlocal word1, word2
            return 0 if word1[a] == word2[b] else 1
        
        
        def distance(a: int, b: int) -> int:
            nonlocal memo
            if a < 0: return b+1
            if b < 0: return a+1
            
            if memo[a][b] != -1:
                return memo[a][b]
            
            memo[a][b] = min(distance(a-1,b)+1, distance(a,b-1)+1, distance(a-1,b-1)+cost(a,b))
            return memo[a][b]
        
        
        x = distance(len(word1)-1, len(word2)-1)
        for row in memo: print(row)
        return x
