class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num_removed = 0
        for i, v in enumerate(nums):
            if v == val:
                num_removed += 1
            else:
                nums[i-num_removed] = nums[i]

        return len(nums) - num_removed
