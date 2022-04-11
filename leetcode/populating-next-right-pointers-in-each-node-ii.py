"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        binary tree level order traversal
        node = level.pop(0)
        node.next = level[0]


        """
        if not root:
            return None

        level = [root]
        while level:
            next_level = []
            for i in range(len(level)):
                if i < len(level) - 1:
                    level[i].next = level[i+1]
                else:
                    level[i].next = None

                if level[i].left:
                    next_level.append(level[i].left)
                if level[i].right:
                    next_level.append(level[i].right)

            level = next_level

        return root
        
