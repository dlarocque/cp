# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        preorder: root, left, right
        inorder: left, root, right
        
        preorder[0] is the root of the tree
        inorder[root_val_idx-1] is the left child of the root
         
        """
        if not preorder or not inorder:
            return None
        
        root_val = preorder[0]
        inorder_idx = inorder.index(root_val)   
        
        right = self.buildTree(preorder[inorder_idx+1:], inorder[inorder_idx+1:])
        left = self.buildTree(preorder[1:inorder_idx+1], inorder[:inorder_idx])
        return TreeNode(root_val, left, right)
