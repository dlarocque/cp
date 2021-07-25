class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        minCount, maxCount = 1001, 0
        for c in s:
            count = s.count(c)
            minCount = min(minCount, count)
            maxCount = max(maxCount, count)
        return minCount == maxCount
