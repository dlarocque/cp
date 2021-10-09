class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        idx = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx] = nums[i]
                idx += 1

        while idx < len(nums):
            nums[idx] = 0
            idx += 1

