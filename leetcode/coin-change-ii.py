class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Coin problem

        This is a slightly more difficult variation of the coin problem, since
        the order of the coins do not matter- we are looking at combinations.

        If the order did matter (i.e. we were not looking at combinations), 
        then we could apply a simple extension of coin change 1

        Since the order does not matter, we can place coins in the same positions
        and reach the correct answer. In this solution, we maintain the order of the 
        coins that we are given.

        1+1+2 would be one of our combinations
        1+1+2+2 would be one of our combinations
        1+2+1 would not, since 1's can not follow 2's

        This makes sure that our combinations are distinct.

        Find all the ways to reach each amount from 1,n with the each coin in 
        order from left to right in the list, incrementing the number of ways to reach
        each coin as we reach them, eventually finding our solution.
        """
        dp = [0]*(amount+1)
        dp[0] = 1
        
        for val in coins:
            for amt in range(1, amount+1):
                dp[amt] += dp[amt-val]

        return dp[amount]
