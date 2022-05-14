class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        Optimize for maximum number of courses taken
        
        
        Brute Force:
        Try all of the possible valid course schedules (permutations of courses), return the most we were able to complete
        O(n!) time complexity 
        
        
        Greedy:
        Select the course that has the earliest lastDay
        
        """
        durations = []
        start, end = 0, 0
        for duration, deadline in sorted(courses, key=lambda c: c[1]):
            heapq.heappush(durations, -duration) # max heap
            end += duration
            if end > deadline: # can't finish this course by the deadline
                end += heapq.heappop(durations) # greedily remove the course with longest duration
        
        return len(durations)
