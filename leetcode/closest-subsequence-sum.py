class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        """
        The problem here lies is that the O(2^n) solution does not pass,
        but the O(2^(N/2)) solution does.
        Think, 2^40 vs. 2^20 is a massive difference.
        
        1. Create two sorted lists of the sums of all subsequences of nums split in half
            Call these A, B
        2. Perform a binary search on each sum in A to find the smallest Abs difference
          > O(2^(n/2)logn), since we do binary search 2^(n/2) times.
        
        """
        n = len(nums)
        
        def dfs(i: int, curr: int, arr: List[int], sums: set) -> None:
            if i == len(arr):
                sums.add(curr)
                return
            dfs(i+1, curr, arr, sums)
            dfs(i+1, curr+arr[i], arr, sums)
        
        a, b = set(), set()
        dfs(0, 0, nums[:n//2], a)
        dfs(0, 0, nums[n//2:], b) 
        b = sorted(b)
                
        min_diff = math.inf
        
        # binary search for the closest val in B for each s in A
        for s in a:
            remain = goal - s
            i = bisect_left(b, remain) # index where we'd insert remain into to keep sorted
            if i < len(b):
                min_diff = min(min_diff, abs(remain-b[i]))
            if i > 0:
                min_diff = min(min_diff, abs(remain-b[i-1]))
                
        
        return min_diff
