class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
                """
        0/1 Knapsack problem does not apply when we have k knapsacks
        Another approach we can try is the DFS solution
        > This could work, since the constraints for nums is rather small 
          compared to Partition Subset Sum (was n<=200)
          
        DFS Approach
        1. if we find a set that sums to target, dfs with remaining nums, decrement
           the number of sets that we need, it the dfs returns true, then return true
        2. if there are no subsets of nums that sum to target, return false
        
        Time:  O(n^2)
        Space: O(n^2)
        
        Recurring sub-problem?
        """
        n, target = len(nums), sum(nums)
        if target % k != 0 or k > n:
            return False
        
        target /= k
        
        def dfs(nums: List[int], curr: int, sets_rem: int) -> bool:
            nonlocal target
            
            if curr > target:
                return False
            
            if curr == target:
                if not nums:
                    return True
                sets_rem -= 1
                curr = 0
                
                if sets_rem == 0:
                    return True
                
            
            
            for idx, num in enumerate(nums):
                if dfs(nums[:idx]+nums[idx+1:], curr+num, sets_rem):
                    return True
                
        return dfs(nums, 0, k)
