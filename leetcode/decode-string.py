class Solution:
    def decodeString(self, s: str) -> str:
        current_string = ''
        k = 0
        stack = []

        for char in s:
            if char.isdigit(): 
                k = k * 10 + int(char)
            elif char == '[':
                stack.append((current_string, k))
                current_string = ''
                k = 0
            elif char == ']':
                prev_string, prev_k = stack.pop(-1)
                current_string = prev_string + prev_k * current_string
            else:
                current_string += char 
                
        return current_string
