class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_parens = []
        
        def dfs(parens: str, num_open: int, to_open: int) -> None:
            nonlocal all_parens, n
            
            # we have nothing left open, so close everything
            if to_open == 0:
                parens += ')'*num_open
                all_parens.append(parens)
                return
            
            # we can open more parens
            if num_open < n:
                dfs(parens+'(', num_open+1, to_open-1)
            
            # there is a paren to close
            if num_open > 0:
                dfs(parens+')', num_open-1, to_open)
            
        dfs('', 0, n)
        return all_parens
