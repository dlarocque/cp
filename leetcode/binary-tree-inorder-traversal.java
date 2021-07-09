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
    public List<Integer> inorderTraversal(TreeNode root) {
        
        List<Integer> order = new LinkedList<Integer>();

        if(root == null)
            return order;
        
        // visit the left sub-tree
        if(root.left != null)
            order.addAll(inorderTraversal(root.left));
        
        // visit the root
        order.add(root.val);
        
        // visit the right sub-tree
        if(root.right != null)
            order.addAll(inorderTraversal(root.right));
        
        return order;
    }
}
