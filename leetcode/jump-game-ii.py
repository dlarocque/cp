class Solution:
    def jump(self, nums: List[int]) -> int:
        """Returns the minimum amount of jumps we need to make to reach the end

        - Dynamic Programming

        - Try to extend as far as we can each step
        - Once we pass our limit for a step, we increment the number of steps we've taken
        - If we reach the end, return steps

        Example:
        nums = [2,3,1,1,4]
        steps = 1
        prev_reach = 2
        reach = 2
        """
        n = len(nums)
        if n == 1:
            return 0
        steps, prev_reach, reach = 0, 0, 0

        for i in range(n):
            reach = max(reach, i + nums[i])

            if reach >= n-1:
                return steps+1
            elif i == prev_reach:
                steps += 1
                prev_reach = reach

        return steps

