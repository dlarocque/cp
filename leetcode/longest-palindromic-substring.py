class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, n = '', len(s)

        def expandPadindrome(l: int, r: int) -> str:
            nonlocal s
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return s[l+1:r]

        for i in range(n):
            odd = expandPadindrome(i, i)
            even = expandPadindrome(i, i+1)

            if len(res) < len(odd):
                res = odd
            if len(res) < len(even):
                res = even

        return res
