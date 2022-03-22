class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()        
        res, curr_end = len(points), points[0][1]
        for start, end in points[1:]:
            if start > curr_end:
                curr_end = end
            else: # overlap
                res -= 1
                curr_end = min(curr_end, end)
                    
        return res
