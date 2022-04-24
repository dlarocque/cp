import math
import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(pq)
        right = max(row[0] for row in nums)
        ans = -math.inf, math.inf
        while pq:
            left, row, col = heapq.heappop(pq)
            if right - left < ans[1] - ans[0]:
                ans = left, right

            if col == len(nums[row])-1:
                return ans
            
            next_smallest = nums[row][col+1]
            right = max(right, next_smallest)
            heapq.heappush(pq, (next_smallest, row, col+1))

