class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        res, n = [], new_interval

        for idx, i in enumerate(intervals):
            if i[1] < n[0]: # interval is before new interval
                res.append(i)
            elif n[1] < i[0]: # interval is after new interval
                res.append(n)
                return res+intervals[idx:]
            else: # interval overlaps with new interval
                n[0] = min(i[0], n[0])
                n[1] = max(i[1], n[1])

        res.append(n)

        return res
