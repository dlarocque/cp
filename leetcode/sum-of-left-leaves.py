# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.preorder(root, False)
        return self.sum

    def preorder(self, root, is_left):
        if root is None:
            return

        # if left leaf node, add to sum
        if is_left and not root.right and not root.left:
            self.sum += root.val

        self.preorder(root.left, True)
        self.preorder(root.right, False)
