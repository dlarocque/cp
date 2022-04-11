# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Left-to-right level order traversal, adding rightmost node at every level
        """
        if not root:
            return root

        level, view = [root], []
        while level:
            view.append(level[-1].val)
            next = []
            for node in level:
                if node.left: next.append(node.left)
                if node.right: next.append(node.right)
        
