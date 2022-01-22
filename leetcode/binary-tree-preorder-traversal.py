# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        def preorder(root: Optional[TreeNode], path: List[int]) -> None:
            if not root:
                return 
            
            path.append(root.val)
            preorder(root.left, path)
            preorder(root.right, path)
            
        res = []
        preorder(root, res)
        return res
