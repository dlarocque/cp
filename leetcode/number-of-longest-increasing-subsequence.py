class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lengths, count = [1]*n, [1]*n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[i] == lengths[j]:
                        lengths[i] = lengths[j]+1
                        count[i] = count[j]
                    elif lengths[i] == lengths[j]+1:
                        count[i] += count[j]

        return sum([count[i] for i in lengths if i == max(lengths)])

