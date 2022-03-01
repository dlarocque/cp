class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPal(s: str) -> bool:
            return s[::-1] == s

        
        def dfs(i: int, path: List[int]) -> None:
            nonlocal res, s
            if i == len(s):
                res.append(path)
                return

            for j in range(i, len(s)):
                if isPal(s[i:j+1]):
                    dfs(j+1, path+[s[i:j+1]])
            

        dfs(0, [])
        return res
