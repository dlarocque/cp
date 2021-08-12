class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        self.min_cost = [-1] * (len(cost) + 1)
        self.min_cost[0], self.min_cost[1] = 0, 0
        return self.minCost(len(cost))

    def minCost(self, k: int) -> int:
        minus_one = -1
        minus_two = -1

        if self.min_cost[k-1] != -1:
            minus_one = self.min_cost[k-1]
        else:
            minus_one = self.minCost(k-1)
        if self.min_cost[k-2] != -1:
            minus_two = self.min_cost[k-2]
        else:
            minus_two = self.minCost(k-2)

        self.min_cost[k] = min(minus_one + self.cost[k-1], minus_two + self.cost[k-2])
        return self.min_cost[k]
