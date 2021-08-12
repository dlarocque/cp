# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # DFS (inorder traversal)
        # Compute sum of path at each node
        # If we find the target, return True
        return self.hasPathSumHelper(root, 0, targetSum)

    def hasPathSumHelper(self, root: TreeNode, pathSum: int, targetSum: int) -> bool:
        if root is None:
            return False

        pathSum += root.val
        if pathSum == targetSum and root.left is None and root.right is None:
            return True

        if self.hasPathSumHelper(root.left, pathSum, targetSum) or self.hasPathSumHelper(root.right, pathSum, targetSum):
            return True

        return False

