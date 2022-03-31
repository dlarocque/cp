class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        lo, hi = 0, n-1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            if nums[mid] == target:
                return True
            
            while lo < mid and nums[mid] == nums[lo]:
                lo += 1
                
            # mid is part of left side
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid-1
                else:
                    lo = mid+1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1
                
        return False
