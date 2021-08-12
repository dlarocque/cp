class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        num_open_parens = 0
        string = ''
        skip_next = False
        for c in s[1:]:
            if skip_next:
                skip_next = False
                continue
            if c == '(':
                num_open_parens += 1
                string += c
            elif num_open_parens != 0:
                num_open_parens -= 1
                string += c
            else:
                skip_next = True

        return string
