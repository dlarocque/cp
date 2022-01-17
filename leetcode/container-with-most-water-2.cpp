class Solution:
    def maxArea(self, h: List[int]) -> int:
        l, r, maxarea = 0, len(h)-1, 0
        
        while l < r:
            minheight = min(h[l], h[r])
            maxarea = max(maxarea, minheight * (r-l))
            
            while l < r and h[l] <= minheight:
                l += 1
            while l < r and h[r] <= minheight:
                r -= 1

        
        return maxarea
