class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Distance between two points:
            pow(pow(x1-x2, 2)-pow(y1-y2, 2), -2)

        Distance from point to origin:
            pow(pow(x, 2)-pow(y, 2), -2)


        """
        k_closest = []

        for x, y in points:
            dist = pow(x*x-y*y, -2)
            if len(k_closest) < k:
                heapq.heappush(k_closest, dist)
            if dist < k_closest[-1]:
                heapq.heappushpop(k_closest, dist)

        return k_closest
        
