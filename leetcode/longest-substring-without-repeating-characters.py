class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Return the length of the longest substring without repeating characters

        s = 'abcabcbb'
        dp = [1, 2, 3, 3, 3, 3, ]
        dict = {a:3, b:4, c:5}
        max_len = 3



        Subproblem:
        To determine the longest substring in a string that ends at a given character,
        we need to know the longest substring that ends at the preceeding character in the string,
        and whether or not the current character already exists within that substring.


        """
        start, max_len = 0, 0
        used = {}

        for i, c in enumerate(s):
            if c in used and used[c] >= start:
                start = used[c]+1
            else:
                max_len = max(max_len, i-start+1)
            used[c] = i

        return max_len
