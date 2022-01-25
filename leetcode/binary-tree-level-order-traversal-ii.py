# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [(root, 0)]
        level_order = [] 
        
        while queue:
            node, level = queue.pop(0)
            if level < len(level_order):
                level_order[level].append(node.val)
            else:
                level_order.append([node.val])
            
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        
        return level_order[::-1]
        
