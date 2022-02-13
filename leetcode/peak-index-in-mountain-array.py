class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 1, len(arr)-2

        while l < r:
            m = (l+r) // 2

            # peak is to the right of mid
            if arr[m] < arr[m+1]:
                l = m + 1
            # peak is not to the right of mid, it must be mid or to the left
            else:
                r = m

        return l
