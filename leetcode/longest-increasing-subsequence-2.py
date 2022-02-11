class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Solution 1: BF DFS
        Find all increasing subsequences, return the length of the 
        longest one
        
        Time: O(2^n), as we add a new int, the number of possible subsequences doubles
        Space: O(n), depth of the recursion stack
        
        Solution 2: DFS with caching from right to left
        - dp[i] = LIS that includes nums[i]
        If nums[i]
        
        
        nums = [0,1,0,3,2,3]
        dp =   [ , , ,2,2,1]
        
        Notes:
        - Try brute force solution first, then look for a potential 
        re-use in previously solved sub-problems, instead of instantly
        trying to find a DP solution without even knowing how to solve
        without DP.
        """
        n = len(nums)
        dp = [1] * n
        
        # right to left
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    
        return max(dp)
