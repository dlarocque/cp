class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Brute force solution:
        Compare all of the sub-arrays with the same lengths in both arrays,
        tracking the length of the longest sub-arrays that were equal.

        Decent solution:
        Try to find each element in nums1 in nums2, then extending the length of the
        sub-array that we're comparing by 1, until the sub-arrays are not equal, while adjusting
        some variable that tracks the longest length we've found so far.
        """
        dp = [[0 for _ in range(len(nums2)+1)] for _ in range(len(nums1)+1)]

        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1

        return max(max(row) for row in dp)
