class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num] += 1;
        }
        
        vector<pair<int, int>> freq_arr;
        for (auto p : freq) {
            freq_arr.push_back(p);
        }
        
        // sort array by second val
        sort(freq_arr.begin(), freq_arr.end(), [](const pair<int, int>&a, const pair<int, int>&b){
            return a.second > b.second;
        });
        
        vector<int> result;
        for (int i = 0; i < k; ++i) {
            result.push_back(freq_arr[i].first);
        }
        
        return result;
    }
};
