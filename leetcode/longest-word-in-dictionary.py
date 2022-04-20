class TrieNode:

    def __init__(self):
        self.nodes = {}
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.longest_word = ''

    def insert(self, s: str):
        curr = self.root
        curr_len = 0

        for idx, char in enumerate(s):
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()

                # no prefix 
                if idx != len(s)-1:
                    curr_len = -math.inf  
                # last char in s
                else:
                    curr.nodes[char].is_word = True
                    
            if curr.nodes[char].is_word:
                curr_len += 1

            curr = curr.nodes[char]

        if curr_len > len(self.longest_word):
            self.longest_word = s
        elif curr_len == len(self.longest_word):
            self.longest_word = min(self.longest_word, s)
        

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()

        for word in sorted(words):
            trie.insert(word)

        return trie.longest_word

