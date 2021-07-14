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
        if(root == null)
            return 0;
        
        Queue<TreeNode> node_q = new LinkedList<TreeNode>();
        Queue<Integer> dep_q = new LinkedList<Integer>();
        
        int dep = 1;
        int minDep = Integer.MAX_VALUE;
        node_q.add(root);
        dep_q.add(dep);
        while(node_q.size() > 0 && dep_q.size() > 0) {
            root = node_q.poll();
            dep = dep_q.poll();
            // System.out.println("val " + root.val + " dep " + dep);
            
            // leaf node
            if(root.left == null && root.right == null) {
                minDep = Math.min(dep, minDep);
            } else {
                // internal node, add children to queue
                if(root.left != null) {
                    node_q.add(root.left);
                    dep_q.add(dep+1);
                }
                if(root.right != null) {
                    node_q.add(root.right);
                    dep_q.add(dep+1);
                }                
            }
        }
        return minDep;
    }
}
