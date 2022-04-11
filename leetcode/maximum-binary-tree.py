# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """
        1. Find the maximum value
        2. create new node with max value, assign left and right nodes recursively
        3. return new root node
        """
        if not nums: 
            return None
        root_val = max(nums)
        root_idx = nums.index(root_val)
        left = self.constructMaximumBinaryTree(nums[:root_idx])
        right = self.constructMaximumBinaryTree(nums[root_idx+1:])
        
        return TreeNode(root_val, left, right)
