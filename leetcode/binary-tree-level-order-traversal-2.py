# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        level = queue
        add root to level
        while level is not empty
            nextlevel = queue
            while level is not empty
                nextlevel.enqueue(level.dequeue())
                traversal.appedn
            level = next

        """
        if not root:
            return []
        traversal, level = [], [root]
        while level:
            traversal.append([node.val for node in level])
            next_level = []
            while level:
                node = level.pop(0)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            level = next_level

        return traversal
        
