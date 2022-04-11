# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], min_val=-math.inf, max_val=math.inf) -> bool:
        if not root:
            return True
        
        if root.val >= max_val or root.val <= min_val:
            return False
        
        left = self.isValidBST(root.left, min_val, min(max_val, root.val))
        right = self.isValidBST(root.right, max(min_val, root.val), max_val)
        return left and right
