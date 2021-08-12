# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return self.maxDepthHelper(root, 1)

    def maxDepthHelper(self, root: TreeNode, dep: int) -> int:
        if root is None:
            return 0

        return max(dep, self.maxDepthHelper(root.left, dep+1), self.maxDepthHelper(root.right, dep+1))
