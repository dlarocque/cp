class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        
        while lo < hi:
            mid1 = lo + (hi-lo)//2
            mid2 = mid1+1
            if nums[mid1] < nums[mid2]:
                lo = mid2
            else:
                hi = mid1
                
        return lo
                
