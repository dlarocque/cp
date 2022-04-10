class Solution:
    def minimizeResult(self, E: str) -> str:
        n = len(E)
        
        plus = E.index('+')
        
        # initial expression
        min_value = sum(list(map(int, E.split("+"))))
        result = "(" + E + ")"
        
        # search for all possible sub expressions
        for i in range(plus):
            for j in range(n, plus + 1, -1):
                e = E[i:j]   # sub expression
                e1 = E[0:i]  # before the expression
                e2 = E[j:]   # after the expression
                
                value = sum(list(map(int, e.split("+")))) 
                
                # multiply the values, if there are no's before and after the sub-expression
                if e1 != "": value *= int(e1)  
                if e2 != "": value *= int(e2)
                
                # update the min_value
                if(min_value > value):
                    min_value = value
                    result = e1 + "(" + e + ")" + e2                
                
        return result
