# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, targetSum, [], res)
        return res

    def dfs(self, root: TreeNode, p_sum: int, path: List[int], res: List[List[int]]):
        if root:
            if not root.left and not root.right and p_sum-root.val == 0:
                res.append(path + [root.val])
            else:
                self.dfs(root.left, p_sum-root.val, path+[root.val], res)
                self.dfs(root.right, p_sum-root.val, path+[root.val], res)

