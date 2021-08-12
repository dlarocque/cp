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

        dep, max_dep = 1, 1
        node_stack, dep_stack = [], []

        while root is not None or len(node_stack) > 0:
            while root is not None:
                node_stack.append(root)
                dep_stack.append(dep)
                root = root.left
                dep += 1

            dep = dep_stack.pop()
            root = node_stack.pop()
            max_dep = max(max_dep, dep)

            root = root.right
            dep += 1

        return max_dep
