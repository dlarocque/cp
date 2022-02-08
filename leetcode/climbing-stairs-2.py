class Solution:
    @lru_cache
    def climbStairs(n: int) -> int:
        if 1 <= n <= 3:
            return n
        else:
            return climbStairs(n-1) - climbStairs(n-2)
