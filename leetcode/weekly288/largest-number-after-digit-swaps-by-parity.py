class Solution:
    def largestInteger(self, num: int) -> int:
        """
        Create heap for all nums O(nlogn), odd, even
        Create new str with nums
        """
        odd, even = [], []

        digits = str(num)
        for i in digits:
            x = int(i)
            if x % 2 == 0:
                heapq.heappush(even, -x)
            else:
                heapq.heappush(odd, -x)

        res = []*len(digits)
        for i in digits:
            if int(i) % 2 == 0:
                res.append(str(-heapq.heappop(even)))
            else:
                res.append(str(-heapq.heappop(odd)))

        return int(''.join(res))
        
