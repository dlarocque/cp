class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        moves, open_parens = 0, 0
        
        for i in range(len(s)):
            match s[i]:
                case '(':
                    open_parens += 1
                case ')':
                    if open_parens > 0:
                        open_parens -= 1
                    else:
                        moves += 1
            
        return moves + open_parens
