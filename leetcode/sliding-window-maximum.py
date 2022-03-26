class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        queue = []
    
        for i in range(n):
            # starting position of the current window
            start_idx = i + 1 - k
            
            while queue and i-queue[0] >= k:
                queue.pop(0)
            
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop(-1)
                
            queue.append(i)
            
            if start_idx >= 0:
                res.append(nums[queue[0]])
        
        return res
    
