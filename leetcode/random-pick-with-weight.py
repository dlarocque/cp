class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [w[0]]
        for i, x in enumerate(w[1:]):
            self.prefix.append(self.prefix[i]+x)
            
    def pickIndex(self) -> int:
        target = self.prefix[-1] * random.random()
        
        # find the index of the first number greater than target
        # e.g. [0,3,7,10,13], target = 4
        l, r, m = 0, len(self.prefix)-1, -1
        while l < r:
            m = l + (r - l)//2
            
            # everything to the right of m is not our index
            if self.prefix[m] > target:
                r = m
            else:
                l = m + 1
                
        #print(target, l, self.prefix)
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
