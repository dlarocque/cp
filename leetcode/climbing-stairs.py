class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        dp = [-1] * (n+1)
        for i in range(0, 4):
            dp[i] = i

        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
