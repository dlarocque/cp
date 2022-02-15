class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Silly solution:
        1. Square all of the nums in the list
        2. Sort the numbers and return the list
        Time: O(nlogn)
        Spacec: O(1)
        """
        res = collections.deque()
        l, r = 0, len(nums)-1
        
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                res.appendleft(left**2)
                l += 1
            else:
                res.appendleft(right**2)
                r -= 1
        
        return res
