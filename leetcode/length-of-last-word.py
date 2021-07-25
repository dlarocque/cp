class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()

        if len(words) < 1:
            return 0

        return len(s.split()[-1])
