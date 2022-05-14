class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n, k, word_length = len(s), len(words), len(words[0])
        substr_size = k * word_length
        indices = []
        word_count = collections.Counter(words)
        
        def sliding_window(left: int) -> None:
            words_found = collections.defaultdict(int)
            words_used = 0
            excess_word = False
            
            for right in range(left, n, word_length):
                if right+word_length > n:
                    break
                    
                sub = s[right:right+word_length] # next word we're adding to the window
                if sub not in word_count:
                    # invalid window, move left to the end of the current window and reset
                    words_found = collections.defaultdict(int)
                    words_used = 0
                    excess_word = False
                    left = right + word_length
                else:
                    # contract window while it's too large or we have an excess word
                    while right-left == substr_size or excess_word:
                        leftmost_word = s[left:left+word_length]
                        left += word_length
                        words_found[leftmost_word] -= 1
                        if words_found[leftmost_word] == word_count[leftmost_word]:
                            excess_word = False
                        else:
                            words_used -= 1
                            
                    words_found[sub] += 1
                    if words_found[sub] <= word_count[sub]:
                        words_used += 1
                    else:
                        excess_word = True
                        
                    if words_used == k and not excess_word:
                        indices.append(left)
        
        for left in range(word_length):
            sliding_window(left)
            
        return indices
