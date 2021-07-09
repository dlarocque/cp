class Solution {
public:
    void reverseString(vector<char>& s) {
        // two pointer approach
        int l = 0;
        int r = s.size() - 1;
        
        char temp;
        while(l < r) {
            temp = s[r];
            s[r] = s[l];
            s[l] = temp;
            ++l;
            --r;
        }
    }
};
