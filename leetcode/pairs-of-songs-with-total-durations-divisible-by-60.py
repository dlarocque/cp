class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rem = [0] * 60
        res = 0

        for t in time:
            print(t % 60)
            res += rem[-t % 60]
            rem[t % 60] += 1
        return res
