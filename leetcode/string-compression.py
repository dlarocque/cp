class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        next_pos = i
        while i < len(chars):
            j = i+1
            while j < len(chars) and chars[i] == chars[j]:
                j += 1

            chars[next_pos] = chars[i]
            next_pos += 1
            num_consecutive = j-i

            if num_consecutive > 1:
                digits = list(str(num_consecutive))
                chars[next_pos:next_pos+len(digits)] = digits
                next_pos += len(digits)

            i = j

        chars = chars[0:next_pos]

        return next_pos
