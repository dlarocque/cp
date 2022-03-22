class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = []
        
        a_idx = ord('a') - 1
        i, to_add = n-1, 0
        while i >= 0:
            if k-i >= 26:
                to_add = (k-i)//26
                res = res + ['z' for _ in range(to_add)]
                k -= to_add*26
                i -= to_add
            elif k > i:
                to_add = k - i
                res.append(chr(to_add+a_idx))
                k = i 
                i -= 1
            else:
                to_add = 1
                res.append('a')
                i -= 1
                
        return ''.join(res[::-1])
    
