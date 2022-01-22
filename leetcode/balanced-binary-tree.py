# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # print(self.tree_depth(root.left), self.tree_depth(root.right))
        
        if abs(self.tree_depth(root.left) - self.tree_depth(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        

    def tree_depth(self, root: Optional[TreeNode], depth=0) -> int:
        if not root:
            return depth
        
        return max(self.tree_depth(root.left, depth+1,), self.tree_depth(root.right, depth+1))
