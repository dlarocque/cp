class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        res = []
        intervals.append(new_interval)

        for i in sorted(intervals):
            if res and res[-1][1] >= i[0]:
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)

        return res
