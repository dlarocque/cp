class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False
        
        l1, l2 = len(s), len(t)
        if l1 > l2:
            return self.isOneEditDistance(t, s)
        
        if l2 - l1 > 1:
            return False
        
        for i in range(l1):
            if s[i] != t[i]:
                # Insert s[:i] == t[i+1:]
                # Replace s[i+1:] == t[i+1:]
                print(s[:i], t[:i+1])
                return s[i:] == t[i+1:] or s[i+1:] == t[i+1:]
        
        return True
                    
