class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1

        while lo <= hi:
            mid = (hi + lo)//2

            if nums[mid] == target:
                return mid

            # mid is in left sorted portion
            if nums[mid] >= nums[lo]:
                if target > nums[mid] or target < nums[lo]:
                    lo = mid+1
                else:
                    hi = mid-1
            # mid is in right-sorted portion
            else:
                if target < nums[mid] or target > nums[hi]:
                    hi = mid-1
                else:
                    lo = mid+1

        return -1
