class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # False if there's any overlap between the meetings
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True
