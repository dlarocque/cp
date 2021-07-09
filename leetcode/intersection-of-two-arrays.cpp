class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> intersection;
        // store the uniques from both arrays
        unordered_map<int, int> exists;
        for(int i = 0; i < nums1.size(); i++) {
            exists[nums1[i]] = ++exists[nums1[i]];
        }
        
        for(int i = 0; i < nums2.size(); i++) {
            if(exists[nums2[i]]) {
                intersection.push_back(nums2[i]);
                --exists[nums2[i]];
            }
        }
        
        return intersection;
    }
};
