class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        number of combinations:
        (n! - k!) / k!
        
        - We have n choices for the first number, n-1 choices for the second number
        ... n-(k+1) choices for the last number in each combination
        
        """
        combinations = []
        
        def dfs(nums: List[int], combination: List[int], remaining_nums: int) -> None:
            if remaining_nums == 0:
                nonlocal combinations
                combinations.append(combination)
                return
            
            for i in range(len(nums)):
                dfs(nums[:i], combination+nums[i], remaining_nums-1)
                
        nums = [[i] for i in range(1, n+1)]
        dfs(nums, [], k)
        return combinations
                
