# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Count the number of nodes that are good
        -A node is good if there are no nodes between the node and the root,
        where node.val > curr_node.val (including the root itself)

        Solution
        - Traverse the tree (recursively, inorder)
        - Track the largest node in the path from root to the current node, at each
            level of recursion

        """
        self.good = 0
        self.dfs(root, float('-INF'))
        return self.good


    def dfs(self, root: TreeNode, max_val: int) -> None:
        if root.val >= max_val:
            self.good += 1

        if root.left: self.dfs(root.left, max(max_val, root.val))
        if root.right: self.dfs(root.right, max(max_val, root.val))
