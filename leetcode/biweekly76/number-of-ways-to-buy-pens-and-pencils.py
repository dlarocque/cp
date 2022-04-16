class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        # total = 20, cost1 = 10, cost2 = 5
        res = 0

        def dfs(amt: int) -> int:
            if amt <= 0:
                return 1
    
            nonlocal cost2
            return 1 + amt//cost2

        
        while total >= 0:
            res += dfs(total)
            total -= cost1

        return res
