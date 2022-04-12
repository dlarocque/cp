class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        nums = [1,3,5,4,7]
        """
        n = len(nums)
        res = 0
        length, count = [0]*n, [0]*n
        for i in range(n):
            for j in range(i):
                # We can append nums[i] to the subs. that ends at j
                if nums[i] > nums[j]:
                    if length[i] + 1 == length[j]:
                        length[i] = length[j]
                        count[i] = count[j]
                    elif length[i] == length[j]:
                        pass
        return res

