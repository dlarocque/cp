class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        overflow = False
        for i, digit in enumerate(digits[::-1]):
            # carry over
            print(i, digit)
            if digit == 9:

                digits[len(digits) - 1 - i] = 0

                if i == len(digits)-1:
                    digits.insert(0, 1)
                    return digits
            else:
                digits[len(digits) - i - 1] += 1
                return digits
