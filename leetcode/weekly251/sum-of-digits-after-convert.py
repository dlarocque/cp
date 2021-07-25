class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = ""
        for c in s:
            asc = str(ord(c) - 96)
            nums += asc

        res = 0
        for i in range(k-1):
            x = 0
            for c in nums:
                x += eval(c)

            nums = str(x)

        for i in range(len(nums)):
            res += eval(nums[i])

        return res

