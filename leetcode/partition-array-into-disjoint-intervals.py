class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        max_from_left = [nums[0]] * len(nums)
        left_end_idx = 0

        for i in range(1, len(nums)):
            max_from_left[i] = max(max_from_left[i-1], nums[i])

            # we need to add this to the left sub-array
            if nums[i] < max_from_left[left_end_idx]:
                left_end_idx = i

        return left_end_idx + 1
