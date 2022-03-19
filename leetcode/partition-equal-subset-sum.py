class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        num_sum = sum(nums)
        if num_sum & 1 == 1:
            return False

        goal_sum = num_sum // 2
        reach = [[False for _ in range(goal_sum+1)] for _ in range(len(nums)+1)]
        
        # base case
        reach[0][0] = True

        for i in range(1, len(nums)+1):
            for _sum in range(goal_sum+1):
                reach[i][_sum] = reach[i-1][_sum]
                if _sum >= nums[i-1]:
                    reach[i][_sum] = reach[i][_sum] or reach[i-1][_sum-nums[i-1]]

        return reach[-1][goal_sum]
