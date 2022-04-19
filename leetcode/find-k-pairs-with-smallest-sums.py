class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        nums1 = [1,7,11], nums2 = [2,4,6], k = 3
        """
        h, res = [], []

        # initialize the min heap
        for idx, num in enumerate(nums1):
            h.append((num+nums2[0], idx, 0))
            
        i = 0
        while i < k and h:
            _, idx1, idx2 = heapq.heappop(h)
            if idx2 < len(nums2)-1:
                heapq.heappush(h, (nums1[idx1]+nums2[idx2+1], idx1, idx2+1))

            res.append([nums1[idx1], nums2[idx2]])
            i += 1

        return res
        
