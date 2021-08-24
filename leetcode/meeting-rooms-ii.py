class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """Determine the minimum number of meeting rooms we need

        [[2,4],[3,8],[7,10]]
        min_rooms = 2
        end_times = [8, 10]


        1. Sort the intervals according to their start times O(nlogn)
        2. Place meetings in rooms, storing their ending times in a minheap insertion
        3. If a meeting starts after the earliest ending time, pop from the heap and
        check again O(logn)
        4. If a meeting starts before the earliest ending time, insert that ending time in the heap
        and check if we need to adjust our min_rooms O(logn)

        """

        intervals.sort() # sort by meeting starting times
        end_times = [intervals[0][1]]
        min_rooms = 1

        for meeting in intervals[1:]:
            while end_times and meeting[0] >= end_times[0]:
                heapq.heappop(end_times)
            heapq.heappush(end_times, meeting[1])
            min_rooms = max(min_rooms, len(end_times))

        return min_rooms


