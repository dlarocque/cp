# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        if not root:
            return False
        
        def dfs(root, path_sum) -> bool:
            if not root:
                return False
            nonlocal target_sum
            
            # leaf node, check sum
            if not root.left and not root.right:
                return (path_sum+root.val == target_sum)
            else:
                return dfs(root.left, path_sum+root.val) or dfs(root.right, path_sum+root.val)
                
        return dfs(root, 0)
