class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0

        start, end, max_end = 0, 0, 0

        for jumps in range(n):
            end = max_end
            while start < n-1 and start <= end:
                if start + nums[start] >= n-1:
                    return jumps+1

                max_end = max(max_end, start+nums[start])

                start += 1

