# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Recursively calculate the largest sum from each root to predecessors of left and right children
        If leftsum and rightsum are positive, set maxpathsum = max(maxpathsum, leftsum+rightsum)
        Else if either are positive
            maxpathsum = max(maxpathsum, positive pathsum)
            
        
        """
        max_path_sum = -math.inf
        
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal max_path_sum
            if not node:
                return 0
            
            left_path_sum = dfs(node.left)
            right_path_sum = dfs(node.right)
            
            if left_path_sum > 0 and right_path_sum > 0:
                max_path_sum = max(max_path_sum, left_path_sum+right_path_sum+node.val)
                return max(left_path_sum, right_path_sum) + node.val
            elif left_path_sum > 0:
                max_path_sum = max(max_path_sum, left_path_sum+node.val)
                return left_path_sum + node.val
            elif right_path_sum > 0:
                max_path_sum = max(max_path_sum, right_path_sum+node.val)
                return right_path_sum + node.val
            else:
                max_path_sum = max(max_path_sum, node.val)
                return node.val
            
        
        dfs(root)
        return max_path_sum
