# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        stack = [root]
        res = [[root.val]]

        while len(stack) > 0:
            # for each node in the level
            level = []
            for _ in range(len(stack)):
                root = stack.pop()
                if len(res)%2 == 0:
                    if root.left: level.append(root.left)
                    if root.right: level.append(root.right)
                else:
                    if root.right: level.append(root.right)
                    if root.left: level.append(root.left)

            if len(level) > 0:
                res.append([node.val for node in level])
            stack = level

        return res
