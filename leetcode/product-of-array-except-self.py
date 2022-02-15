
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        - Must be O(n) time
        - Can not use the division operation
        
        1. Create prefix and suffix arrays
            prefix[i] = product of nums[0...i-1]
            suffix[i] product if nums[i+1...n-1]
        2. Create the answer array, where
            answer[i] = prefix[i] * suffix[i]
            
        Time: O(n)
        Space O(n)
        """
        n = len(nums)
        prefix, suffix = [1]*n, [1]*n
        
        # prefix array
        for idx in range(1, n):
            prefix[idx] = prefix[idx-1]*nums[idx-1]
            
        # suffix array
        for idx in range(n-2, -1, -1):
            suffix[idx] = suffix[idx+1]*nums[idx+1]
            prefix[idx] *= suffix[idx]
        
        return prefix
