class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(curr_sum: int, idx: int) -> int:
            nonlocal nums, target, memo
            
            if (idx, curr_sum) in memo:
                return memo[(idx, curr_sum)]
            
            if idx < 0:
                if curr_sum == target:
                    return 1
                else:
                    return 0
            
            memo[(idx, curr_sum)] = dfs(curr_sum+nums[idx], idx-1) + dfs(curr_sum-nums[idx], idx-1)
            return memo[(idx, curr_sum)]
    
        return dfs(0, len(nums)-1)
