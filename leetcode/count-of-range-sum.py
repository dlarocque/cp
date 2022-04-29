import collections


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        cumsum = [0]*n
        running_sum = 0
        res = 0
        for idx, num in enumerate(nums):
            running_sum += num
            cumsum[idx] = running_sum
            
        record = collections.defaultdict(int)

        """
        [-2,5,-1]
        cumsum = [-2,3,2]
        record:
            -2: 1
            3: 1
            2: 1
        """
        for csum in cumsum:
            for target in range(lower, upper+1):
                # can cut the prefix sum csum, with another, earlier prefix sum of value csum-target, to have a range of sum of target
                # csum - (csum-target) = target
                if csum-target in record:
                    res += record[csum-target]

            record[csum] += 1 

        return res
                    
                    
