import math, collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ''

        t_freqs = collections.defaultdict(int)
        for c in t:
            t_freqs[c] += 1

        min_window_l, min_window_r = -math.inf, math.inf
        l, r = 0, 0
        freqs = collections.defaultdict(int)
        completed, required = 0, len(t_freqs.keys())

        while r < m:

            # move right
            freqs[s[r]] += 1

            # update the number of completed chars we have
            if freqs[s[r]] == t_freqs[s[r]]:
                completed += 1

            # move left until the window is invalid
            while l <= r and completed == required:
                # check if the current valid window is the smallest
                if r - l < min_window_r - min_window_l:
                    min_window_r, min_window_l = r, l

                # character is no longer part of our window, update its frequency
                freqs[s[l]] -= 1

                # a character is no longer complete
                if freqs[s[l]] == t_freqs[s[l]] - 1:
                    completed -= 1
                
                l += 1 # contract window

            r += 1 # move window outwards

        return s[min_window_l:min_window_r+1] if min_window_l != -math.inf and min_window_r != math.inf else ""

