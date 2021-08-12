class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last_jump = n-1 # the shortest jump we need to be able to make to make it to the end

        for idx in range(n-2, -1, -1):
            if idx + nums[idx] >= last_jump:
                last_jump = idx
        return last_jump == 0
