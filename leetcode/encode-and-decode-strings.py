class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.

        Encode each char in each word as its ascii value
        end of a word will be represented by -1
        """
        encoding = []
        for i, s in enumerate(strs):
            char_encodings = []
            for c in s:
                char_encodings.append(str(ord(c)))
                char_encodings.append('-')
            char_encodings = char_encodings[:-1]
            encoding.append(''.join(char_encodings))
        return ' '.join(encoding)


    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        decoding = []
        words = s.split(' ')
        print(words)
        for word in words:
            vals = word.split('-')
            chars = []
            print(vals)
            for val in vals:
                if val: chars.append(chr(int(val)))
            decoding.append(''.join(chars))

        return decoding


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
