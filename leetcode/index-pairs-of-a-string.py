class TrieNode:
    def __init__(self):
        self.nodes, self.is_word = {}, False
            
    @staticmethod
    def construct_trie(words: List[str]):
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.nodes:
                    node.nodes[char] = TrieNode()
                node = node.nodes[char]
            node.is_word = True
            
        return root
    
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        index_pairs, trie = [], TrieNode.construct_trie(words)
        
        for l in range(len(text)):
            node = trie
            for r in range(l, len(text)):
                if text[r] not in node.nodes:
                    break
                node = node.nodes[text[r]]
                if node.is_word:
                    index_pairs.append([l, r])
                    
        return index_pairs
