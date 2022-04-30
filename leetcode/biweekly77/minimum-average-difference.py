class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        avg_suffix, avg_prefix = [0]*n, [0]*n
        
        run = 0
        for idx, val in enumerate(nums):
            run += val
            avg_prefix[idx] = int(run / (idx+1))
            
        run = 0
        for idx in range(n-2, -1, -1):
            run += nums[idx+1]
            avg_suffix[idx] = int(run / (n-idx-1))
        
        min_diff = math.inf
        res = 0
        for idx in range(n):
            if abs(avg_prefix[idx]-avg_suffix[idx]) < min_diff:
                min_diff = abs(avg_prefix[idx]-avg_suffix[idx])
                res = idx
                

        return res
            
        
