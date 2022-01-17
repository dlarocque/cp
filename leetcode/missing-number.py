class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        nums = [x,x,x,x,x,x,x,7,9] (sorted)
        
        
        1. sort O(nlogn)
        2. a form of binary search (logn)
             > if nums[mid] == mid
                    left side is good
                    right side is bad
                    ... go to mid of right side
                else
                    left side is bad
                    right side is good
                    ... go to mid of left side
        """
        for idx, val in enumerate(sorted(nums)):
            if idx != val:
                return val-1
            
        return len(nums)
