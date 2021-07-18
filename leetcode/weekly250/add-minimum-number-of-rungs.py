class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        res = 0
        if rungs[0] > dist:
            res = (rungs[0]-1) // dist

        for i in range(len(rungs)-1):
            if (rungs[i]+dist) < rungs[i+1]:
                res = res + ((rungs[i+1]-rungs[i]-1) // dist)

        return res
