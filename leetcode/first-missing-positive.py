class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Optimal Solutions:
            1. Cycle Sort
            2. Use indices as hashes
        """
        n = len(nums)
        i = 0
        while i < n:
            j = nums[i]-1
            if 0 <= j < n and nums[i] != nums[j]:
                nums[j], nums[i] = nums[i], nums[j]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i+1:
                return i+1

        return n+1

    def firstMissingPositive2(self, nums: List[int]) -> int:
        """
        Original solution, not optimal- should be at most a medium if this is AC
        Time: 10 minutes
        """
        seen = set()
        fmp = 1
        for num in nums:
            seen.add(num)
            while fmp in seen:
                fmp += 1
        
        return fmp
