class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        lo = 1
        hi = (x//2) + 1
        while True:
            mid = (hi + lo) // 2
            mid_sq = mid*mid
            midp1_sq = (mid+1)*(mid+1)
            if mid_sq <= x < midp1_sq:
                return mid
            elif mid_sq > x:
                hi = mid
            elif mid_sq < x:
                lo = mid
