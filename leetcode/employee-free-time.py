import heapq # Definition for an Interval.
class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule):
        """
        Merge all intervals with a Heap of the earliest shifts from all 
        """
        h = [(row[0].start, row[0].end, i, 0) for i, row in enumerate(schedule)]
        heapq.heapify(h)
        merged_hours = []

        while h:
            start, end, row, col = heapq.heappop(h)

            # there is overlap, extend the last interval
            if merged_hours and start <= merged_hours[-1].end:
                merged_hours[-1].end = max(merged_hours[-1].end, end)
            # create a new interval
            else:
                merged_hours.append(Interval(start, end))

            # add the next interval to the heap
            if col+1 < len(schedule[row]):
                heapq.heappush(h, (schedule[row][col+1].start, schedule[row][col+1].end, row, col+1))

        # merged_hours contains all the hours worked by all employees
        # return the intervals that are not in merged_hours
        res = []
        for i in range(len(merged_hours)-1):
            res.append(Interval(merged_hours[i].end, merged_hours[i+1].start))

        return res

