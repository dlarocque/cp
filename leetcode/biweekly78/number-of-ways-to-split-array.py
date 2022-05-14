class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        """
        prefix and suffix sum
        
        """
        n = len(nums)
        res = 0
        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(prefix[-1]+nums[i])
            
        #print(prefix)
        #suffix = [nums[-1]]
        running_sum = 0
        for i in range(n-2, -1, -1):
            
            running_sum += nums[i+1]
            #print(running_sum)
            if prefix[i] >= running_sum:
                res += 1
        
        return res
