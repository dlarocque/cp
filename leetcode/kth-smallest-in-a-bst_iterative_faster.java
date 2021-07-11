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
        LinkedList<TreeNode> stack = new LinkedList<TreeNode>();
        
        while(root != null || stack.size() != 0) {
            while(root != null) {
                stack.addFirst(root);
                root = root.left;
            }
            root = stack.removeFirst();
            if(--k == 0) {
                break;
            }
            root = root.right;
        }
        return root.val;
    }
}
