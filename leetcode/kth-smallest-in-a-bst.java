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
    public int kthSmallest(TreeNode root, int k) {
        return inorderTraversal(root).get(k-1);
    }
    
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> order = new ArrayList<>();
        
        if(root == null)
            return order;
        
        if(root.left != null)
            order.addAll(inorderTraversal(root.left));
        
        order.add(root.val);
        
        if(root.right != null)
            order.addAll(inorderTraversal(root.right));
        
        return order;
    }
}
