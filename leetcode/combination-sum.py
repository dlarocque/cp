class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates, target, res, [])
        return res

    def dfs(self, nums, target, res, path):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        else:
            for i in range(len(nums)):
                if nums[i] > target:
                    continue
                self.dfs(nums[i:], target-nums[i], res, path+[nums[i]])
