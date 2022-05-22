class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok == '+': stack.append(stack.pop(-1) + stack.pop(-1))
            elif tok == '-': stack.append(stack.pop(-2)-stack.pop(-1))          
            elif tok == '/': stack.append(int(stack.pop(-2)/stack.pop(-1)))
            elif tok == '*': stack.append(stack.pop(-1) * stack.pop(-1))                           
            else: stack.append(int(tok))
                    
        return stack[-1]
    
    
