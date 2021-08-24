class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        level = coins[:]
        next_level = []
        visited = [False] * (amount+1)
        dep = 0
        while level:
            dep += 1

            for denom in level:
                if denom == amount:
                    return dep
                elif denom < amount:
                    for coin in coins:
                        if denom+coin <= amount and not visited[denom+coin]:
                            next_level.append(denom+coin)
                            visited[denom+coin] = True


            next_level, level = [], next_level

        return -1
