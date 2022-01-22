class Solution:
    def minDistance(self, text1: str, text2: str) -> int:
        """
        1. dynamic programming
         > 2d array for all possible combinations of both strings
         > dp[i][j] represents the lcs for text1[0:i+1], text2[0:j+1]
        
            sub-problems:
            (1) if text1[i] == text2[j], then we know that the lcs 
                is going to be the lcs of the string that excludes those
                two characters, plus one (dp[i-1][j-1])
            (2) else, the lcs is going to the lcs that we've found already
                which is max(dp[i-1][j], dp[i][j-1])
                
        ^^^ From longest-common-subsequence.py
        
        Extension:
        If we know the length of the longest common subsequence, then 
        we can sum the difference between the length of the two strings
        and the longest common subsequence.
        
        The longest common subsequence will be the resulting string after
        the deletions.
        """
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
              
        return n + m - (2*dp[-1][-1])
