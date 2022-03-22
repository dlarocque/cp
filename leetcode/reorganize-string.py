class Solution:
    def reorganizeString(self, s: str) -> str:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        
        pq = [(-freq, char) for char, freq in d.items()]
        heapq.heapify(pq)
        
        res = []
        prev_freq, prev_char = 0, ''
        while pq:
            freq, char = heapq.heappop(pq)
            res.append(char)
            
            if prev_freq < 0:
                heapq.heappush(pq, (prev_freq, prev_char))
            
            prev_freq, prev_char = freq+1, char
        
        return ''.join(res) if len(res) == len(s) else ''
        
