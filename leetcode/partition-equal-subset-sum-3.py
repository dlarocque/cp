class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target & 1 == 1:
            return False

        target >>= 1 # divide by 2
        possible = [True] + [False]*target
        
        for weight in nums:
            for k in range(target, -1, -1): # right to left
                if possible[k] and k+weight <= target:
                    possible[k+weight] = True
                                            
        return possible[target]
