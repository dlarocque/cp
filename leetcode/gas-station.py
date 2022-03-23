class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        One-pass solution
        Not really a greedy problem, and a bit of a niche solution
        
        Big idea
         - If sum(gas) > sum(cost), there exists a solution
         
        From left to right, let's accumulate gas
        If we run out of gas, restart at the next gas station
        
        When we reach the end, let's check to see if we have accumulated 
        enough gas to make it all the way back around to before our starting point
        (curr_gas >= prev)
        If we don't have enough gas, we don't have a solutionp
         
        """
        res, prev, curr_gas = 0, 0, 0
        for i in range(len(gas)):
            curr_gas += gas[i] - cost[i]
            if curr_gas < 0:
                res = i+1
                prev += curr_gas
                curr_gas = 0
        
        return res if curr_gas+prev >= 0 else -1
