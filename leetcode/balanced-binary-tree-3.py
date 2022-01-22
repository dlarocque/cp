# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        time: O(n)
        space: O(n) recursion stack
        
        """
        
        def check(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            left = check(root.left)
            if left == -1:
                return -1
            right = check(root.right)
            
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1
        
        return check(root) != -1
