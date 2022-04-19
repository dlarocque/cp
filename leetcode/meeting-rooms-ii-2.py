class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        queue maintaining the end times of the current conferences

        iterate over intervals in the order of their start times
            while first element in queues end time is smaller than the new start time
                dequeue
            enqueue current interval 
            update max intersections

        return max intersections
        """
        max_intersections = 0
        current_intervals = []

        for start, end in sorted(intervals, key=lambda x: x[0]):
            while current_intervals and current_intervals[0] <= start:
                heapq.heappop(current_intervals)

            heapq.heappush(current_intervals, end)
            max_intersections = max(max_intersections, len(current_intervals))

        return max_intersections
