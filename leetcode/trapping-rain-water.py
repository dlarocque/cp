class Solution:
    def trap(self, h: List[int]) -> int:
        """
        Similar problem: Container with most water

        Two-pointer solution
        Ideas:
        - If we know a lower bound (l_max, r_max), we can determine the max amount of water 
          that we can hold.
        - If we know that l_max < r_max, we know l_max will be our lower bound. vice-versa
        - If l_max < r_max, we know that we can't make a higher "wall"
          by moving right, since l_max will be our lower bound.
          So, we move left while accumulating water from that left lower bound.

        O(n) time, O(1) space
        """
        res = 0
        l, r = 0, len(h)-1
        l_max, r_max = h[l], h[r]
        while l < r:
            l_max = max(l_max, h[l])
            r_max = max(r_max, h[r])
            if l_max < r_max:
                res += l_max - h[l]
                l += 1
            else:
                res += r_max - h[r]
                r -= 1
        
        return res
