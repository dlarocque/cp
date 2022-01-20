class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        1. Dynamic programming
         > 2D array for all possible combinations of both strings
         > dp[i][j] represents the LCS for text1[0:i+1], text2[0:j+1]
        
            Sub-problems:
            (1) If text1[i] == text2[j], then we know that the LCS 
                is going to be the LCS of the string that excludes those
                two characters, plus one (dp[i-1][j-1])
            (2) Else, the LCS is going to the LCS that we've found already
                which is max(dp[i-1][j], dp[i][j-1])
        """
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
                        
        return dp[-1][-1]
