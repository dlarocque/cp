# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        Solution 1: 
        1. First pass of the tree, building a list of nodes in each level
        2. Iterate through the list that we've created, and take the averages
        
        Example 1:
        1.
        [(3,1),(29,2),(22,2)]
        2.
        [[3],[14.5],[11]]
        
        Time: O(n) with two passes
        Space: O(m) extra space, m is the depth of the tree
        
        One pass solution: 
        visit one level at a time and compute the average at every level
        
        """
        level_averages = []
        
        # level-order traversal
        level, nodes_in_level = [root], 1
        while len(level) > 0:
            level_sum = 0
            nodes_in_next_level = 0
            for i in range(nodes_in_level):
                node = level.pop(0)
                level_sum += node.val
                
                if node.left:
                    nodes_in_next_level += 1
                    level.append(node.left)
                
                if node.right:
                    nodes_in_next_level += 1
                    level.append(node.right)
                
            level_averages.append(level_sum / nodes_in_level)
            nodes_in_level = nodes_in_next_level
        
        return level_averages
