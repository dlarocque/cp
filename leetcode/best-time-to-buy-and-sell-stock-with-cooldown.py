class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Brute force solution:
        Find all the combinations of stocks that we can buy and sell and
        return the max profit among those.
        
        Three states
        s0 = waited cooldown, can buy or not buy
        s1 = just bought, can sell or not sell
        s2 = just sold, can only wait for cooldown -> s0
        """
        if len(prices) == 1:
            return 0
        
        buy, sell, hold = 0, -prices[0], 0
        for i in range(1, len(prices)):
            next_buy = max(buy, hold)
            next_sell = max(sell, buy-prices[i])
            hold = sell+prices[i]
            buy = next_buy
            sell = next_sell
            
        return max(buy, sell, hold)
