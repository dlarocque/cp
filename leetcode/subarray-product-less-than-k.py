class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n, left, res, prod = len(nums), 0, 0, 1
        
        for right in range(n):
            prod *= nums[right]
            while prod >= k and left <= right:
                prod /= nums[left]
                left += 1
            
            res += right - left + 1 # number of subarrays from left...right
            
        return res
            
