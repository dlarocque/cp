class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.combinations = []
        self.dfs(sorted(candidates), target, [])
        return self.combinations

    def dfs(self, candidates: List[int], target: int, combination: List[int]) -> None:
        if target == 0:
            self.combinations.append(combination)
        elif target > 0:
            for idx, val in enumerate(candidates):
                if idx > 0 and candidates[idx] == candidates[idx-1]:
                    continue
                elif val > target:
                    break
                else:
                    self.dfs(candidates[idx+1:], target-val, combination+[val])
