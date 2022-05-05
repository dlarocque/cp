class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
        Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
        Explanation: 
        Window position                Median
        ---------------                -----
        [1  3  -1] -3  5  3  6  7        1
         1 [3  -1  -3] 5  3  6  7       -1
         1  3 [-1  -3  5] 3  6  7       -1
         1  3  -1 [-3  5  3] 6  7        3
         1  3  -1  -3 [5  3  6] 7        5
         1  3  -1  -3  5 [3  6  7]       6

        Maintain a heap of the elements in the current window
        O(logk) every time the heap moves (n-k times)
        Time: O((n-k)logk), Space: O(k)
            
        Notes:
        - n-k sliding windows
        """

        
