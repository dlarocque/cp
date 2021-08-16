class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map sets of chars to indices of their lists of anagrams
        anagram_indices = {}
        anagrams = []

        for string in strs:
            letters = ''.join(sorted(string))
            idx = anagram_indices.get(letters)
            if idx is not None:
                anagrams[idx].append(string)
            else:
                anagrams.append([string])
                anagram_indices[letters] = len(anagrams)-1

        return anagrams
