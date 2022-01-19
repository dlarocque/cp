class Solution: def countSubstrings(self, s: str) -> int: """
        1. Palindromes can have two different middle points
            ...x... or ...xx...
        2. Iterate over every character in the string, and expand all possible middle points (i,i) and (i,i+1), iterating our solution every time we successfully expand either of them
        """
        res = 0
        
        def extend_palindrome(s: str, start: int, end: int):
            nonlocal res
            
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
                res += 1
        
        for idx in range(len(s)):
            extend_palindrome(s, idx, idx)
            extend_palindrome(s, idx, idx+1)
        
        return res
