import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Brute Force:
            Idea: Examine all possible paths, increment when pathsum = targetSum
            Time: O(n^2)
            Space: O(h), where h is the height of the tree


        Optimization:
            We re-use tree nodes many times when calculating the sum of all possible paths.
            Is there a way that we can only visit the value of a node once?
            > If we know there is a path from root...x with sum old_sum,
              and our current path from root...curr with sum curr_sum,
              and curr_sum - old_sum == target,
                We know there is an intermediate path from x...curr with sum that equals target.

        Optimal Solution:
            Idea: DFS + Prefix sum
            Time: O(n)
            Space: O(h), where h is the height of the tree
        """
        old_sum = collections.defaultdict(int)
        num_paths = 0
        
        def dfs(node: TreeNode, curr_sum: int) -> None:
            nonlocal old_sum, num_paths, targetSum
            if not node:
                return
            
            curr_sum += node.val
            if curr_sum == targetSum:
                num_paths += 1
            
            num_paths += old_sum[curr_sum - targetSum]

            old_sum[curr_sum] += 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            old_sum[curr_sum] -= 1

        dfs(root, 0)
        return num_paths
        
