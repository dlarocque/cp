# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        # Case 1: root is p or q, so it's the LCA
        if root == p:
            return p
        if root == q:
            return q

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # Case 2: p and q are in different sub-tree, so root is the LCA
        if left and right:
            return root

        # Case 3: p and q are the same sub-tree, so return the outcome of that sub-problem
        return left or right
