# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BFS using queue
        - store columns in a dictionary in order of depth, then move to a list
        - using a dictionary for simplicities sake
        - in-order traversal to maintain depth order with queue
        
        """
        if not root:
            return []
        queue = [(root, 0)]
        d = {}
        
        while queue:
            node, idx = queue.pop(0)
            
            if idx in d:
                d[idx].append(node.val)
            else:
                d[idx] = [node.val]
                
            if node.left:
                queue.append((node.left, idx-1))
            if node.right:
                queue.append((node.right, idx+1))
                        
        res = [d[idx] for idx in sorted(d.keys())]
        return res
        
