// O(n) time, O(n) space
class Solution {
    public int maxSubArray(int[] nums) {
        int a[] = new int[nums.length];
        a[0] = nums[0];
        int max = a[0];
        
        for(int i = 1; i < nums.length; i++) {
            a[i] = Math.max(nums[i], a[i-1]+nums[i]);
            max = Math.max(a[i], max);
        }
        
        return max;
    }
}

// Solution without storing all the previous max sub-arrays
// * A little harder to understand
// O(n) time (faster than 100%), O(1) space
class Solution {
    public int maxSubArray(int[] nums) {
        if(nums.length == 0)
            return 0;
        if(nums.length == 1)
            return nums[0];

        int runSum = nums[0]; // The maximum sum of the array from 0 to i
        int max = runSum;

        for(int i = 1; i < nums.length; i++) {
            runSum = Math.max(nums[i], runSum+nums[i]);
            max = Math.max(max, runSum);
        }
        
        return max;
    }
}
