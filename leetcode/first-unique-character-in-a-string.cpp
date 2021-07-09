class Solution {
public:
    int firstUniqChar(string s) {
        // key is the char
        // pair.first is the frequency of the char
        // pair.second is the index of that char
        unordered_map<char, pair<int, int>> m;
        
        for (int i = 0; i < s.size(); i++) {
            m[s[i]].first++;
            m[s[i]].second = i;
        }
        
        int idx = s.length();
        // visit all the mappings
        for(auto &p : m) {
            // find the pair with p.first > 0, and smallest p.second
            if(p.second.first == 1) {
                idx = min(idx, p.second.second);
            }
        }
        
        if(idx == s.length()) {
            return -1;
        }
        return idx;
    }
};
