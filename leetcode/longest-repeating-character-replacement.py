class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_char_count = max_window_size = 0 # frequency of the most frequently occuring char in the window
        count = collections.Counter()
        
        for idx, char in enumerate(s):
            count[char] += 1
            max_char_count = max(max_char_count, count[char])
            
            # if true, then we found a new largest valid window
            if max_window_size - max_char_count < k:
                max_window_size += 1
            # shift the window to the left by updating the counter of the leftmost char
            else:
                count[s[idx - max_window_size]] -= 1
                            
        return max_window_size
    
