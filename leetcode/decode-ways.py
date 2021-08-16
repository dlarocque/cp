class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [0] * (n+1)

        # base case
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, n+1):
            single = int(s[i-1:i])
            double = int(s[i-2:i])

            if 0 < single <= 9:
                dp[i] += dp[i-1]
            if 10 <= double <= 26:
                dp[i] += dp[i-2]

        return dp[n]

