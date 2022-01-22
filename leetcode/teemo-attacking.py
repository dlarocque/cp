class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        """
        Once poisoned: poisoned from timeSeries[i] to timeSeries[i] + duration - 1
        """
        total_seconds = 0
        
        for i in range(len(timeSeries)):
            total_seconds += duration
            
            if i > 0 and timeSeries[i] <= timeSeries[i-1]+duration-1:
                total_seconds -= timeSeries[i-1] + duration - timeSeries[i] # difference
            
        return total_seconds
