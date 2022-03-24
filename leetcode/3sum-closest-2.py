class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res, n = math.inf, len(nums)
        nums.sort()
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lo, hi = i+1, n-1
            while lo < hi:
                tsum = nums[i] + nums[lo] + nums[hi]
                if abs(tsum-target) < abs(res-target):
                    res = tsum
                if tsum < target:
                    lo += 1
                elif tsum > target:
                    hi -= 1
                else:
                    return tsum
                
        return res
