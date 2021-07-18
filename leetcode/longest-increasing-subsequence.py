class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxlen = 0
        length = []
        for i in range(len(nums)):
            length.append(1)
            for j in range(i):
                if(nums[i] > nums[j]):
                    length[i] = max(length[i], length[j]+1)
            maxlen = max(length[i], maxlen)

        return maxlen
