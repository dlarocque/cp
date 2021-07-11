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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> sol = new LinkedList<List<Integer>>();
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        
        if(root == null)
            return sol;
        
        queue.add(root);
        while(!queue.isEmpty()) {
            int nodesInLevel = queue.size();
            
            // add the children of all the nodes in the level from left to right
            // nodes will be added to the solution from left to right in the level
            List<Integer> level = new LinkedList<Integer>();
            for(int i = 0; i < nodesInLevel; i++) {
                if(queue.peek().left != null)
                    queue.offer(queue.peek().left);
                if(queue.peek().right != null)
                    queue.offer(queue.peek().right);
                
                level.add(queue.poll().val);
            }
            
            sol.add(level);
        }
        
        return sol;
    }
}
