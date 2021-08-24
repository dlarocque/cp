class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            if 0x1 & n == 1:
                res += 1
            n = n >> 1
        return res
