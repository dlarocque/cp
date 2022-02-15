class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Solution 1:
        1. Create an array a=[1,2,3,...,n]
        2. Iterate through nums, a.remove(nums[i])
        3. return resulting array a
        
        Time: O(n^2) -> iterate through nums O(n), removing from array O(n)
        Space: O(n)
        
        Solution 2:
        1. Create a dict d, d[1,...n: 1]
        2. Iterate through nums, d.remove(nums[i])
        3. Return list(d.keys())
        
        Time: O(n) -> iterate through nums O(n), removing from dict O(1)
        Space: O(n)
        """
        d = {}
        n = len(nums)
        
        # 1
        for i in range(1, n+1):
            d[i] = 1
        
        # 2
        for i in nums:
            if i in d: d.pop(i)
        
        # 3
        return list(d.keys())
