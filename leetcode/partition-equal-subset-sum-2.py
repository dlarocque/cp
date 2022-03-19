class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        num_sum = sum(nums)
        if num_sum & 1 == 1:
            return False

        num_sum >>= 1 # divide by 2
        dp = [True] + [False]*num_sum
        for num in nums:
            dp = [dp[x] or (x-num >= 0 and dp[x-num]) for x in range(num_sum+1)]
            
        return dp[num_sum]

