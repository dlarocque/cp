class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        BFS 
        Search the possible sums of denominations, while avoiding searching
        already found sums
        """
        if amount == 0: return 0
        level = list(coins)
        next_level = []
        visited = {}
        
        dep = 0
        while level:
            dep += 1

            for denom in level:
                if denom == amount:
                    return dep
                elif denom < amount:
                    for coin in coins:
                        if denom+coin <= amount and denom+coin not in visited:
                            next_level.append(denom+coin)
                            visited[denom+coin] = True

            level = next_level
            next_level = []

        return -1

