class Solution:
    def validPalindrome(self, s: str) -> bool:
        deleted = False
        
        def isPalindrome(l: int, r: int) -> bool:
            while l < r and s[l] == s[r]:
                l += 1
                r -= 1
            return l >= r
        
        left, right = 0, len(s)-1
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        
        if left < right:
            return isPalindrome(left+1, right) or isPalindrome(left, right-1)
        
        return True
