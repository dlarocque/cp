class Solution:
    def uniqueLetterString(self, s: str) -> int:
        sum_unique_chars, n = 0, len(s)
        dp = [[0]*n for _ in range(n)]        
        
        def count_unique_chars(t: str):
            d, count = {}, 0
            
            for c in t:
                if c in d:
                    if d[c] == 1:
                        count -= 1
                        d[c] = -1
                else:
                    d[c] = 1
                    count += 1
            
            return count
        
        # iterate over all of the substrings of s
        for i in range(len(s)):
            for j in range(i, len(s)):
                # print(s[i:j+1], count_unique_chars(s[i:j+1]))
                d[i][j] = count_unique_chars(s[i:j+1])
            
        return sum_unique_chars