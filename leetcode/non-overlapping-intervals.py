class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Greedy solution:

        Main Idea: Sort intervals by end time, iterate over intervals, select the intervals with the earliest end times.

        Why?
        It helps to imagine that we want to choose the most non-overlapping intervals possible.
        
        When choosing the first interval (from the left), which one will allow us to choose the most intervals in the future?
        - The interval with the earliest start time.
        * It is not possible for any other interval from the left to allow for more intervals
        ... Apply this to the next interval from the left at every interval, then we have the solution.

        """
        cnt, end = 0, -5*10**4
        
        for s, e in sorted(intervals, key=lambda x: x[1]):
            if s >= end:
                end = e
            else:
                cnt += 1
        
        return cnt
