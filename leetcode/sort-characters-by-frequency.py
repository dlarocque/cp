class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return s
        
        s = sorted(list(s))
        strs = []
        cur_sb = [s[0]]
        for c in s[1:]:
            if cur_sb[-1] != c:
                strs.append("".join(cur_sb))
                cur_sb = []
                
            cur_sb.append(c)
            
        strs.append("".join(cur_sb))
        strs.sort(key=lambda string : len(string), reverse=True)
        return "".join(strs)
