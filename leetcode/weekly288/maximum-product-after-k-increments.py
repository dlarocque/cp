class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        """
        Incrementing the smallest always increases product the most
        """
        h = []
        # create heap
        for i in nums:
            x = int(i)
            heapq.heappush(h, x)

        # increment nums
        for i in range(k):
            heapq.heappush(h, heapq.heappop(h)+1)

        # create sum
        m = 10**9 + 7
        res = 1
        for i in h:
            res *= i
            res %= m

        return res
