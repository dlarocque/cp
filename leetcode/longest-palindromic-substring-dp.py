class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            
        longest_pal_start = 0
        longest_pal_len = 1
        for end in range(1, n):
            for start in range(end-1, -1, -1):
                if s[start] == s[end]:
                    if start == end-1 or dp[start+1][end-1]:
                        dp[start][end] = True
                        if end-start+1 > longest_pal_len:
                            longest_pal_len = end-start+1 
                            longest_pal_start = start
        
        return s[longest_pal_start:longest_pal_start+longest_pal_len]
