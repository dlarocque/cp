class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        d = {}
        d['2'] = ["a", "b", "c"]
        d['3'] = ["d", "e", "f"]
        d['4'] = ["g", "h", "i"]
        d['5'] = ["j", "k", "l"]
        d['6'] = ["m", "n", "o"]
        d['7'] = ["p", "q", "r", "s"]
        d['8'] = ["t", "u", "v"]
        d['9'] = ["w", "x", "y", "z"]

        res = d[digits[0]]

        for digit in digits[1::]:
            letters = d[digit]
            new_res = []
            for letter in letters:
                for num in res:
                    new_res.append(num + letter)
            res = new_res

        return res
