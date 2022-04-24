class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        """
        If we know the lowest common ancestor of start and dest nodes
            the path from start to dest is reverse(path_to_start) + path_to_dest *from that ancestor

        1. Find the LCA
        2. Get paths from both nodes to from the LCA
        3. Return reverse_and_invert(path_to_start) + path_to_dest
        
        Idea:
            - If the first k directions from root to start and dest are the same, 
                the LCA can be reached by following those k directions
                > Trim those first k directions, and we have the paths we need


                3
            1
        2       4

        startValue = 2, destValue = 4
        path_to_start = 'R'
        path_to_end = 'R'
        return 'RR'
        """

        def dfs_directions(node: TreeNode, target: int, prev_step: str) -> str:
            if not node:
                return ''
            if node.val == target:
                return prev_step
            
            left = dfs_directions(node.left, target, 'L')
            if left:
                return prev_step + left
            
            right = dfs_directions(node.right, target, 'R')
            if right:
                return prev_step + right
            
            return ''

        path_to_start = dfs_directions(root, startValue, '')
        path_to_end = dfs_directions(root, destValue, '')
        i = 0
        while i < min(len(path_to_end), len(path_to_start)) and path_to_start[i] == path_to_end[i]:
            i += 1
        
        return 'U' * (len(path_to_start) - i) + path_to_end[i:]
