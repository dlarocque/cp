# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        """
        We can recursively remove children by setting root.left and root.right
        to the return values of the recursive function, that returns None if we
        want to cut the children.
        
        In this case, we want to cut the children if the node is to be deleted.
        So, we only return the root (don't delete childen pointers) if the root
        is not to be deleted.
        
        This is a pretty straight forward traversal problem with a condition.
        """
        delete = set(to_delete)
        roots = []
        
        def traverse(root: Optional[TreeNode], is_root: bool):
            if not root:
                return None
            
            if is_root and not root.val in delete:
                roots.append(root)
                
            root.left = traverse(root.left, root.val in delete)
            root.right = traverse(root.right, root.val in delete)
    
            if root.val in delete:
                return None
            else:
                return root
            
        traverse(root, True)
        return roots
        
