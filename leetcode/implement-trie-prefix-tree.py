class TrieNode:

    def __init__(self, value: chr, children: dict, terminates: bool):
        self.value = value
        self.children = children
        self.terminates = terminates

class Trie:

    def __init__(self):
        """Initialize the Trie to have a root node """
        self.root = TrieNode('*', {}, True)

    def insert(self, word: str) -> None:
        """Inserts a word into the trie. """
        curr = self.root
        while word and word[0] in curr.children:
            curr = curr.children[word[0]]
            word = word[1:]

        while word:
            curr.children[word[0]] = TrieNode(word[0], {}, False)
            curr = curr.children[word[0]]
            word = word[1:]

        curr.terminates = True

    def search(self, word: str) -> bool:
        """Returns if the word is in the trie.

        Traverse the trie, return false if not all the character
        exist in a sub-tree, or if the last character is not terminating.
        True otherwise
        """
        curr = self.root
        while word and word[0] in curr.children:
            curr = curr.children[word[0]]
            word = word[1:]

        # the trie does not contain the word
        if word:
            return False

        # the trie contains the prefix, not the word
        return curr.terminates

    def startsWith(self, prefix: str) -> bool:
        """Returns if there is any word in the trie that starts with the given prefix. """
        curr = self.root
        while prefix and prefix[0] in curr.children:
            curr = curr.children[prefix[0]]
            prefix = prefix[1:]

        if prefix:
            return False

        return True




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
