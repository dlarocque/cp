class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)

        for i in range(len(s)):
            for word in wordDict:
                if s[i-len(word)+1:i+1] == word:
                    if i+1 == len(word) or (i >= len(word)-1 and dp[i-len(word)]):
                        dp[i] = True


        return dp[-1]
