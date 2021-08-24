class TrieNode:

    def __init__(self):
        self.terminates = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        t = self.trie
        for c in word:
            if c not in t.children:
                t.children[c] = TrieNode()
            t = t.children[c]

        t.terminates = True

    def search(self, word: str) -> bool:
        return self.dfs(word, self.trie)

    def dfs(self, word, t) -> bool:
        """
        [['a']]
        word =  '.'

        t: # -> #

        """
        for i, c in enumerate(word):
            if c == '.':
                for val in t.children.values():
                    if self.dfs(word[i+1:], val):
                        return True
                return False

            elif c not in t.children:
                return False
            else:
                t = t.children[c]

        return t.terminates


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
