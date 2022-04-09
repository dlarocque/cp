class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        In-order traversal, return the kth element in the traversal


        """
        def dfs(node: TreeNode):
            nonlocal k
            if not node:
                return None

            left = dfs(node.left)
            if left: 
                return left

            k -= 1
            print(f"k: {k}, node.val: {node.val}")
            if k == 0:
                return node

            right = dfs(node.right)
            if right:
                return right

        kth_smallest = dfs(root)
        return None if not kth_smallest else kth_smallest.val

        
