class Solution:
    def checkValidString(self, s: str) -> bool:
        p_stack = []
        s_stack = []

        for i in range(len(s)):
            if s[i] == '(':
                p_stack.append(i)
            elif s[i] == ')':
                if len(p_stack) > 0:
                    p_stack.pop()
                elif len(s_stack) > 0:
                    s_stack.pop()
                else:
                    return False
            else:
                s_stack.append(i)

        # try to use all of our stars
        for i in p_stack[::-1]:
            for j in s_stack[::-1]:
                if i < j:
                    p_stack.remove(i)
                    s_stack.remove(j)
                    break

        return len(p_stack) == 0
