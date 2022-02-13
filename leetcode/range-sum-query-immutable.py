class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.prefix = [0]*self.n
        
        # compute the prefix sum array (O(n) time)
        self.prefix[0] = self.nums[0]
        for idx in range(1, self.n):
            self.prefix[idx] = self.prefix[idx-1] + self.nums[idx]
            
    def sumRange(self, left: int, right: int) -> int:
        """
        Use the prefix sum array for O(1) time sumRange call
        
        e.g. left = 2, right = 4
        
        nums = [-2, 0, 3, -5, 2, -1]
        sum = prefix[right] - prefix[left-1]
        
        """
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
