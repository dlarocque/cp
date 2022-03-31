class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        lo = bisect_left(arr, x) - 1 
        hi = lo + 1
        while hi - lo -1 < k:
            if lo == -1:
                hi += 1
                continue
            
            if hi == len(arr) or abs(x-arr[lo]) <= abs(x-arr[hi]):
                lo -= 1
            else:
                hi += 1

        return arr[lo+1:hi]
