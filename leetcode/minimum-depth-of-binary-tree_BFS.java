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
    public int minDepth(TreeNode root) {
        if(root == null) return 0;
        
        int dep = 1;
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        while(!q.isEmpty()) {
            int nodesInLevel = q.size();
            for(int i = 0; i < nodesInLevel; i++) {
                root = q.poll();
                if(root.left == null && root.right == null)
                    return dep;
                if(root.left != null)
                    q.offer(root.left);
                if(root.right != null)
                    q.offer(root.right);
            }
            dep++;
        }
        return dep;
    }
}
