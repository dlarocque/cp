class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        Longest common subsequence with reversed string 
        
        
        Palindromes can have two middle points:
            1. ...xx...
            2. ...x...
            
        If we can find all of the palindromic subsequences, then we can find
        the length of the longest one.
        
        To find all palindromes: 
        - Expand each possible middle point in s
        ... extending to subsequences
        if s[left] == s[right]:
            left -= 1, right += 1
        else:
            left -= 1 (for reach right)
        
        s = "bbbab"
        left = 0
        right = 4
        
        max_len = 4
        
        Time: O(n^3)
        Space: O(1)
        """
        s_r = s[::-1]
        n = len(s)
        
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == s_r[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        return dp[-1][-1]
