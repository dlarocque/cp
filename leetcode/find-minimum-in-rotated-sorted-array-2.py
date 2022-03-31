class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        
        n = len(nums)
        lo, hi = 0, n-1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            # pivot is on the right side
            if nums[mid] > nums[hi]:
                lo = mid+1
            # pivot is on the left side
            else:
                # nums[mid] <= nums[hi]
                hi = mid
                
        return nums[lo]
