# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_dep = 0
        
        def dfs(root, dep):
            if not root:
                return
            nonlocal max_dep
            
            if not root.left and not root.right:
                max_dep = max(max_dep, dep)
            else:
                dfs(root.left, dep+1)
                dfs(root.right, dep+1)
        
        dfs(root, 1)
        return max_dep
