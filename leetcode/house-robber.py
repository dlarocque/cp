class Solution:
    def rob(self, nums: List[int]) -> int:
        """Find out what's the maximum amount of money we can get from robbing nums houses

        DP

        Iteratively adjust the maximum amount of money we can get from robbing the last house,
        and not robbing the last house.
        The maximum amount of money we can get from robbing a given house is the max between
        robbing this house and the max money we can get from not robbing the last house and the
        max amount of money we can get from robbing the last house

        """
        not_rob_prev, rob_prev = 0, 0
        for i in range(len(nums)):
            rob_prev, not_rob_prev = max(not_rob_prev+nums[i], rob_prev), rob_prev
        return max(rob_prev, not_rob_prev)

