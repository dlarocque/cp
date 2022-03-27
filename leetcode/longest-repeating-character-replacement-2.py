from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        max_freq stores the most frequent character we've seen in a window so far

        """
        res = max_freq = start = 0
        cnt = Counter()

        for end, char in enumerate(s):
            cnt[char] += 1
            max_freq = max(max_freq, cnt[char])

            if end - start + 1 - max_freq < k:
                cnt[s[start]] -= 1
                start += 1

            res = max(res, end-start+1)

        return res

