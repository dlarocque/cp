class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        c = [-1]*(target+1)
        c[0] = 1
        
        def helper(target: int) -> int:
            nonlocal nums, c
            if target < 0:
                return 0
            if c[target] == -1:         
                c[target] = 0
                for num in nums:
                    c[target] += helper(target-num)
            
            return c[target]
        
        return helper(target)
