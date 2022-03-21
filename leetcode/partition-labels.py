class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        """
        res = []
        n = len(s)
        
        # first pass, find the last occurence of all chars in s
        last_occ = {}
        for i in range(n-1, -1, -1):
            if s[i] not in last_occ:
                last_occ[s[i]] = i
        
        # final pass
        start, end = 0, 0
        for i in range(n):
            end = max(end, last_occ[s[i]])
            if i == end:
                res.append(end-start+1)
                start = end+1
                
        return res
