class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        chars = []
        s_string, t_string = "", ""
        
        # determine the result strings
        for c in s:
            if c == '#':
                if len(chars) > 0:
                    chars.pop()
            else:
                chars.append(c)
                
        s_string = ''.join(chars)
        
        chars = []
        for c in t:
            if c == '#':
                if len(chars) > 0:
                    chars.pop()
            else:
                chars.append(c)
                
        t_string = ''.join(chars)
        
        print(t_string, s_string)
        
        return s_string == t_string
