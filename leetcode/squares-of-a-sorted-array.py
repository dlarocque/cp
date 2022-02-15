class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Silly solution:
        1. Square all of the nums in the list
        2. Sort the numbers and return the list
        Time: O(nlogn)
        Spacec: O(1)
        """
        return sorted([i**2 for i in nums])
