class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        
        # binary search for duplicate
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r - l) // 2
            
            if nums[m] < m + 1:
                r = m
            else:
                l = m + 1
            
        return nums[l]
