class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        store pos, neg lists that store the largest negative and positive numbers
        up until a position
        """
        n = len(nums)
        curr_max = curr_min = res = nums[0]

        for i in range(1, n):
            temp = curr_max

            curr_max = max(nums[i], curr_max * nums[i], curr_min * nums[i])
            curr_min = min(temp*nums[i], curr_min*nums[i], nums[i])

            res = max(res, curr_max)

        return res
