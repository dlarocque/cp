class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> pre = vector<int>(nums.size());
        pre[0] = 0;
        pre[1] = nums[0];
        for (int i = 2; i < nums.size(); i++) {
            pre[i] = nums[i-1] * pre[i-1];
        }
        
        vector<int> suf = vector<int>(nums.size());
        suf[nums.size()-1] = 0;
        suf[nums.size()-2] = nums[nums.size()-1];
        for (int i = nums.size()-3; i >= 0; i--) {
            suf[i] = nums[i+1] * suf[i+1];
        }
        
        vector<int> res = vector<int>(nums.size());
        res[0] = suf[0];
        res[nums.size()-1] = pre[nums.size()-1];
        for (int i = 1; i < nums.size()-1; i++) {
            res[i] = pre[i] * suf[i];
        }
        
        return res;
    }
};
