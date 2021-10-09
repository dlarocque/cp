# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        """
        boundary:
        root + left boundary + leaves (left-to-right) + reverse of right boundary'

        left boundary:
        1.roots left child if it exists,
        2.for each node in left boundary
            if node has left child, left child is in left boundary
            else if node has right child, right child is in left boundary
        3. left-most leaf is not in the boundary

        right boundary
        1.roots right child if it exists,
        2.for each node in right boundary
            if node has right child, right child is in left boundary
            else if node has left child, left child is in left boundary
        3. right-most leaf is not in the boundary


        root = [1,null,2,3,4]
        left_leaves = []
        right_leaves = [3,4]
        left_boundary = []
        right_boundary = [2]
        boundary = [1] + [[] + [3,4]] + [2]

        Idea for solution:
        Generate all of the lists we need to build our boundary
        (left boundary, leaves, right boundary)
        - leaves = [left leaves] + [right leaves] (left-to-right)
        """
        if not root.left and not root.right:
            return [root.val]
        left_leaves, right_leaves = [], []
        left_boundary, right_boundary = [], []

        def generate_leaves(root, leaves: List[int], left: bool) -> None:
            """Generate leaves in a binary tree from left to right"""
            if not root:
                return

            if not root.left and not root.right: # leaf
                leaves.append(root)

            if left == True:
                generate_leaves(root.left, leaves, left)
                generate_leaves(root.right, leaves, left)
            elif left == False:
                generate_leaves(root.right, leaves, left)
                generate_leaves(root.left, leaves, left)

        generate_leaves(root, left_leaves, True)
        generate_leaves(root, right_leaves, False)

        def generate_boundary(root, boundary: List[int], leaves: List[int], left: bool) -> None:
            """Helps generate the boundary of a side of a binary tree"""
            if not root or root is leaves[0]:
                return

            if left:
                boundary.append(root.val)
                if root.left:
                    generate_boundary(root.left, boundary, leaves, True)
                else:
                    generate_boundary(root.right, boundary, leaves, True)
            else:
                boundary.append(root.val)
                if root.right:
                    generate_boundary(root.right, boundary, leaves, False)
                else:
                    generate_boundary(root.left, boundary, leaves, False)

        leaf_values = [node.val for node in left_leaves]

        # generate both sides' boundaries
        generate_boundary(root.left, left_boundary, left_leaves, True)
        generate_boundary(root.right, right_boundary, right_leaves, False)

        # generate the boundary (root + left boundary + leaves (left-to-right) + reverse of right boundary)
        return [root.val] + left_boundary + [node.val for node in left_leaves] + list(reversed(right_boundary))




