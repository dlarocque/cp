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
    public int goodNodes(TreeNode root) {
        // if a nodes val is larger than all of its preceeding nodes' values
        // then it is a good node
        if(root == null)
            return 0;
        
        Stack<TreeNode> stack = new Stack<TreeNode>();
        Stack<Integer> max = new Stack<Integer>();
        int res = 0; 
        int m = 0;
        
        stack.push(root);
        max.push(root.val);
        while(!stack.isEmpty()) {
            root = stack.pop();
            m = max.pop();
            
            if(root.val >= m) {
                // good node
                ++res; 
                m = root.val; 
            }
            
            if(root.left != null) {
                stack.push(root.left);
                max.push(m);
            }
            if(root.right != null) {
                stack.push(root.right);
                max.push(m);
            }
        }
        
        return res;
    }
}
