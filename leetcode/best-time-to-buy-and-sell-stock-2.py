class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        
        left = [math.inf]*n
        left[0] = prices[0]
        for i in range(n):
            left[i] = min(left[i-1], prices[i])
        
        right = [-math.inf]*n
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], prices[i+1])
            
        res = 0
        for i in range(n):
            res = max(res, right[i] - left[i])
                    
        return res
