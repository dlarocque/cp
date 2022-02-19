class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        dp = [[[i]] for i in nums]
        
        for i in range(n-2, -1, -1): # decreasing
            for j in range(i+1, n):
                for subset in dp[j]:
                    dp[i].append([nums[i]]+subset)
          
        subsets = [[]]
        for subs in dp:
            for _set in subs:
                subsets.append(_set)
                
        return subsets
