# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Simultaneously traverse both trees:
            If node1 and node2: merge
            If not node1: node2
            If not node2: node1
            
        We can either create a new tree or just move nodes around 
        in one of the trees.
        
        """
        if not root1:
            return root2
        if not root2:
            return root1
        if root2:
            root1.val += root2.val
            
        # merge left sub-tree
        if root1.left:
            if root2.left:
                self.mergeTrees(root1.left, root2.left)
        else:
            if root2.left:
                root1.left = root2.left
                
        # merge right sub-tree
        if root1.right:
            if root2.right:
                self.mergeTrees(root1.right, root2.right)
        else:
            if root2.right:
                root1.right = root2.right
        
        return root1
