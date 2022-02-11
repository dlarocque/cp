class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Classic DP problem
        
        Solution 1: BF DFS
        Iterate over all of the possible subarrays and compute their sum, storing
        some max_sum that we return
        time: O(n^2), since we examine all subarrays
        space: O(1)
        
        Solution 2: BF DFS with caching
        Go from left to right
            
        
        """
        dp = nums[:]
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i]+dp[i-1])        
        
        return max(dp)
