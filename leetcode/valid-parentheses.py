class Solution:
    def isValid(self, s: str) -> bool:
        parens = []
        for paren in s:
            if paren in ['(', '{', '[']:
                parens.append(paren)
            elif len(parens) == 0:
                return False
            elif paren == ')' and parens[-1] == '(':
                parens.pop()
            elif paren == '}' and parens[-1] == '{':
                parens.pop()
            elif paren == ']' and parens[-1] == '[':
                parens.pop()
            else:
                return False

        return len(parens) == 0
