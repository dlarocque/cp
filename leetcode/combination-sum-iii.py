class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if math.factorial(9) - math.factorial(9-k) < n:
            return []

        combinations = []
        
        def dfs(combination: List[int], curr_sum: int, lo: int):
            nonlocal k, n, combinations
            # print(combination, lo)
            if curr_sum == n and len(combination) == k:
                combinations.append(combination)
                return
            elif curr_sum > n or len(combination) > k:
                return

            for i in range(lo, 10):
                dfs(combination+[i], curr_sum+i, i+1)
                
        dfs([], 0, 1)
        return combinations
