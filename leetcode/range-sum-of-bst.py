# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def traverse(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            _sum = 0
            if low <= root.val <= high:
                _sum += root.val
            _sum += traverse(root.left) + traverse(root.right)
            
            return _sum
        
        return traverse(root) 
