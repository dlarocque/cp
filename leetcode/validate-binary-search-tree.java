/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isValidBST(TreeNode root) {
        LinkedList<TreeNode> stack = new LinkedList<TreeNode>();
        TreeNode previous = null;
        
        while(root != null || stack.size() != 0) {
            while(root != null) {
                stack.addFirst(root);
                root = root.left;
            }
            root = stack.removeFirst();
            if(previous != null && root.val <= previous.val)
                return false;
            previous = root;
            root = root.right;
        }
        return true;
    }
}
