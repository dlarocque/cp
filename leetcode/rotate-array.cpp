class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k %= n;
        
        if(n == k || k <= 0)
            return;
        
        // store all of the nums
        vector<int> store(n);
        for(int i = 0; i < n; i++) {
            store[i] = nums[i];
        }
        
        // place all of the numbers in their new rotated position
        for(int i = 0; i < n; i++) {
            nums[(i + k) % n] = store[i];
        }
    }
};
