class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]

        dp = [0]*len(nums)
        dp[0] = nums[0]

        robbed_prev = True
        if nums[1] < nums[0]:
            dp[1] = nums[0]
            robbed_prev = False
        else:
            dp[1] = nums[1]
        
        for idx in range(2, len(nums)):
            if dp[idx-1] > dp[idx-2] + nums[idx]:
                dp[idx] = dp[idx-1]
                robbed_prev = False
            else:
                dp[idx] = dp[idx-2] + nums[idx]
                robbed_prev = True
    
        return dp[-1]
            
