class Solution:
    def twosum(nums, target):
        d = {}

        for i, v in enumerate(nums):
            if target-v in d:
                return [d[target-v], i]
            else:
                d[num] = i

        return -1
