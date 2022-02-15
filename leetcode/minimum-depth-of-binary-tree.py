# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        min_dep = math.inf
        
        def dfs(root: Optional[TreeNode], dep: int):
            nonlocal min_dep
            if not root:
                return
            if not root.left and not root.right: 
                min_dep = min(min_dep, dep)
            else:
                dfs(root.left, dep+1)
                dfs(root.right, dep+1)
            
        dfs(root, 1)
        return min_dep
