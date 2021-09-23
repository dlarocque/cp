class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        """
        notes
        - order matters
        - if freq of a char in s >= 3, and freq of a char in word in words < 3, skip over char
        - if
        """
        num_stretchy = 0

        for word in words:
            if self.is_stretchy(word, s):
                num_stretchy += 1

        return num_stretchy

    def is_stretchy(self, original: str, stretched: str) -> bool:
        i, j = 0, 0

        while i < len(original) and j < len(stretched):
            if original[i] != stretched[j]:
                return False

            original_rep = self.get_repeat_length(original, i)
            stretched_rep = self.get_repeat_length(stretched, j)

            if original_rep > stretched_rep or (stretched_rep < 3 and stretched_rep != original_rep):
                return False

            i += original_rep
            j += stretched_rep
        return i == len(original) and j == len(stretched)

    def get_repeat_length(self, s, start):
        end = start
        while end < len(s) and s[end] == s[start]:
            end += 1

        return end-start
