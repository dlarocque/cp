class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = needle.size();
        int m = haystack.size();
        for(int i = 0; i <= m - n; i++) {
            int j = 0;
            for(; j < n; j++) {
                if(haystack[i + j] != needle[j])
                    break;
            }
            // loop was not broken, and haystack substr and needle are equal in length
            if(j == n)
                return i;
        }
        
        return -1;
    }
};
