class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        """
        non-overlapping
        non-adjacent

        back-tracking

        Time: O(n^2)
        Space: O(n)
        """
        abbreviations = []

        def dfs(curr_word: str, left: int) -> None:
            if curr_word and left < len(curr_word):
                return

            max_size = len(word) - left
            for size in range(max_size):
                for i in range(len(word) - size):
                    new_word = curr_word[:i] + str(size) + (curr_word[:i+size])
                    dfs(new_word, i+size+1)

        dfs(word, 0)
        return abbreviations


        
