# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursively swap children for each node in the tree
        self.invert(root)
        return root

    def invert(self, root) -> None:
        if not root:
            return
        # swap the children
        temp = root.left
        root.left = root.right
        root.right = temp
        # recursively invert the children
        self.invert(root.right)
        self.invert(root.left)

