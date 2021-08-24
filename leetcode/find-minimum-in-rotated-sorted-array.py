class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        NOTES:
        1. lo + ((hi-lo) // 2) can help us prevent stack overflow in the case where
        our bounds are very large, so it's always safer to do when computing the mid point

        2. When a sorted array is rotated, we know that the right side of that sorted array will always
        contain the smallest element
        e.g. [5,4,1,2,3], [5,4] is the left sorted side, [1,2,3] is the right sorted side

        3. Our goal is to make our bounds smaller until we reach a point where lo is the smallest element,
        and our sub-array is of size 1 (hi == lo)

        4. It is important to always check if we're on the right side first, since in the case where
        our sub-array is fully sorted, our right side comes leftwards.

        Intuition:
        Keep our lower bound on a value that we *know* is to the right of the smallest value (or is the smallest value)
        and iteratively move our upper bound leftwards

        Only move the lower bound upwards when we *know* it is smaller or equal to the smallest value
        i.e. the start of the right side of the rotated sorted array
        """
        lo, hi = 0, len(nums)-1

        while lo < hi:
            m = lo + ((hi-lo) // 2)
            # mid is in the right side of the rotated sorted array
            if nums[m] < nums[hi]:
                # we know that if mid is on the right side of the sorted array,
                # the smallest number will always be on the right side.
                # so, we want to shorten our bounds to get closer to that smallest element
                # since all elements to the right of m are greater than m, we can ignore all of them
                # and set hi = m
                hi = m
            # mid is in the left side of the rotated sorted array
            elif nums[m] > nums[hi]:
                # we know that if mid is in the left side of the sorted array,
                # the smaller number will be on the right side, since the array
                # was rotated
                # so, we try to then enter the right side of the rotated array
                lo = m+1

        return nums[lo]
