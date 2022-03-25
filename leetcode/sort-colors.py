class Solution:
    def sortColors(self, s: List[int]) -> None:
        red_end, white_end, n = 0, 0, len(s)
        # red 
        for i in range(n):
            if s[i] == 0:
                while s[red_end] == 0 and i > red_end:
                    red_end += 1
                
                s[i] = s[red_end]
                s[red_end] = 0
        
        white_end = red_end+1 if s[red_end] == 0 else red_end
        # white
        for i in range(n):
            if s[i] == 1:
                while i > white_end and s[white_end] == 1:
                    white_end += 1
                
                if white_end >= n: return
                
                s[i] = s[white_end]
                s[white_end] = 1
                
