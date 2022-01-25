class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr, _max = 0, 0
        for i in nums:
            if i == 0:
                curr = 0
            else:
                curr += 1
                _max = max(_max, curr)
                
        return _max
