class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        we know all elements at indices > end are odd
        we know all element at indices < start are even
        so, if start == end, our list satisfies the required condition   
        """
        n = len(nums)
        start, end = 0, n-1
        while start < end:
            if nums[start] % 2 == 0:
                start += 1 # we know nums[start] is even, so we move up
            else:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1 # we know nums[end] is now odd, so we move down
            
        return nums
