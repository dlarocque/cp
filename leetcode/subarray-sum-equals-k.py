class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Store all of the integer values that each continuous subarray need to be equal to the sum
        - Map wanted integers to the number of sub-arrays who want them

        [1,2,3] = nums, k = 3
        num_subarrays = 2

        dict
        -3: 1
        -2: 1
        0: 1

        O(n^2) time
        O(n) space
        """
        wanted_count, running_sum, num_subarrays = {0: 1}, 0, 0
        for i in range(len(nums)):
            running_sum += nums[i]
            num_subarrays += wanted_count.get(running_sum-k, 0)
            wanted_count[running_sum] = wanted_count.get(running_sum, 0) + 1

        return num_subarrays
