class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        res = 0

        for word in words:
            badWord = False
            for char in word:
                for brokenChar in brokenLetters:
                    if char == brokenChar:
                        badWord = True
            if badWord == False:
                res = res+1

        return res

