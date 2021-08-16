class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}

        for c in s:
            if c not in d: d[c] = 1
            else: d[c] += 1

        for c in t:
            if c not in d: return False
            else: d[c] -= 1

        for val in d.values():
            if val != 0: return False

        return True
