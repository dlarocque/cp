from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a, b = Counter(), Counter()
        
        for c in s1:
            a[c] += 1
            
        for idx, char in enumerate(s2):
            b[char] += 1
            if idx+1 - len(s1) > 0:
                starting_char = s2[idx-len(s1)]
                b[starting_char] -= 1
                if b[starting_char] == 0:
                    del b[starting_char]
            
            if a == b:
                return True
            
        return False
        
