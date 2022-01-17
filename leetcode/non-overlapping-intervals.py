class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        overlap between x,y if x.start < y.start and x.end > y.start

        """
        cnt, end = 0, -5*10**4
        
        for s, e in sorted(intervals, key=lambda x: x[1]):
            if s >= end:
                end = e
            else:
                cnt += 1
        
        return cnt
