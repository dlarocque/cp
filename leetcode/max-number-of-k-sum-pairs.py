class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Counting the number of pairs of elements in nums that sum to k
        
        Idea:
        d is a dict
        cnt = 0
        for all num in nums
            d[num] += 1
            if d[k - d[num]] > 0
                cnt += 1
                d[num] -= 1
                d[k - d[num]] -= 1
                
        return cnt
        """
        d = {}
        cnt = 0
        for x in nums:
            if k-x in d and d[k-x] > 0:
                d[k-x] -= 1
                cnt += 1
            elif x not in d:
                d[x] = 1
            else:
                d[x] += 1
        
        return cnt
