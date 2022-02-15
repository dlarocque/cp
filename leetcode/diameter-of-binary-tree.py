# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Find the longest path between two nodes
        
        max_dep_right + max_dep_left + 1 = diameter
        """
        if not root:
            return 0
        
        diameter = 0
        
        def dfs(root: Optional[TreeNode], dep: int) -> int:
            if not root:
                return 0
            nonlocal diameter
            left_dep = dfs(root.left, 0)
            right_dep = dfs(root.right, 0)
            
            diameter = max(diameter, left_dep+right_dep)
            
            return max(left_dep, right_dep) + 1
        
        dfs(root, 0)
        return diameter
