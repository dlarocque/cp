class Solution:
    def totalFruit(self, f: List[int]) -> int:
        l, res, count = 0, 0, collections.Counter()
        for r in range(len(f)):
            count[f[r]] += 1
            if len(count) > 2:
                count[f[l]] -= 1
                if count[f[l]] == 0:
                    count.pop(f[l])
            
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
