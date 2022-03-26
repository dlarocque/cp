class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum = nums[0]
        l, r = 0, 0
        min_len = math.inf
        while l <= r and r < len(nums):
            if curr_sum < target:
                r += 1
                if r < len(nums):
                    curr_sum += nums[r]
            else:
                min_len = min(min_len, r - l + 1)
                curr_sum -= nums[l]
                l += 1
                
        return min_len if min_len != math.inf else 0
