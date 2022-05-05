class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """
        Converting to minutes: HH*60 + MM
        
        Notes:
        - Watch out for edge cases at start/eod
        
        Idea:
        1. Convert time to minutes
        2. Sort times in ascending order
        3. Compare times[i+1]-times[i], except times[-1] and times[0] (edge case) 
        
        Time: O(nlogn) time
        Space: O(1) or O(logn), depending on sorting algorithm
        > If we consider sorted list to used extra space, then O(n) space
        
        Edge cases:
        
        """
        n = len(timePoints)
        minutes = sorted([60*int(t[:2])+int(t[3:]) for t in timePoints])
        min_diff = math.inf
        
        for i in range(n-1):
            min_diff = min(min_diff, minutes[i+1]-minutes[i])
            
        # edge case, last comparisons
        min_diff = min(min_diff, (60*24)+minutes[0]-minutes[-1])
        return min_diff
                    
