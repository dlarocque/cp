class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        c_p = sorted(zip([(cost[0] - cost[1]) for cost in costs], costs))
        min_len = 0
        for cf, costs in c_p[int(len(c_p)/2):]: min_len += costs[1]
        for cf, costs in c_p[:int(len(c_p)/2)]: min_len += costs[0]
        return min_len
