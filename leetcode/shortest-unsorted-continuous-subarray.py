import math


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        Two pointer solution
        O(n) time, O(1) space
        """
        n = len(nums)
        
        if n < 2:
            return 0

        def find_min_max(l: int, r: int):
            nonlocal nums, n
            local_min, local_max = math.inf, -math.inf
            for i in range(l, r+1):
                if i >= n:
                    break
                local_min = min(local_min, nums[i])
                local_max = max(local_max, nums[i])
            
            return local_min, local_max
        
        left, right = 0, n-1
        while left < n-1 and nums[left] <= nums[left+1]:
            left += 1

        while right > 0 and nums[right] >= nums[right-1]:
            right -= 1

        if left > right:
            return 0

        local_min, local_max = find_min_max(left, right)
        while left > 0 and nums[left-1] > local_min:
            left -= 1

        while right < n-1 and nums[right+1] < local_max:
            right += 1

        return right-left+1


    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        """
        Sorting solution
        O(nlogn) time, O(n) space
        """
        n = len(nums)
        left, right = 0, n-1

        sorted_nums = sorted(nums)
        while left < right:
            if sorted_nums[left] == nums[left]:
                left += 1

            if sorted_nums[right] == nums[right]:
                right -= 1

        return right-left+1 if left < right else 0
