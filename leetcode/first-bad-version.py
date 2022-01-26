# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        n = 5
        [0,1,1,1,1]
        lo = 1
        mid = 1 
        hi = 1
                
        mid = lo (hi - lo) // 2
                
        
        Sorted array > binary search O(logn)
        time: O(logn)
        space O(1)
        
        """
        lo, hi = 1, n
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            # first bad version is not to our right
            if isBadVersion(mid):
                hi = mid
            # first bad version is not to our left
            else:
                lo = mid+1

            
        return lo
