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
    public int deepestLeavesSum(TreeNode root) {
        int maxDepth = 0;
        int sum = 0;
        int dep = 0;
        LinkedList<TreeNode> nodeStack = new LinkedList<TreeNode>();
        LinkedList<Integer> depStack = new LinkedList<Integer>();
        
        while(root != null || nodeStack.size() != 0) {
            while(root != null) {
                nodeStack.addFirst(root);
                depStack.addFirst(dep);
                root = root.left;
                dep += 1;
            }
            root = nodeStack.removeFirst();
            dep = depStack.removeFirst();
            
            if(dep == maxDepth) {
                sum += root.val;
            } else if(dep > maxDepth) {
                maxDepth = dep;
                sum = root.val;
            }
            root = root.right;
            if(root != null)
                ++dep;
        }
        
        return sum;
    }
}
