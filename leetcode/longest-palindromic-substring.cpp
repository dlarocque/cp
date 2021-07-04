class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.length();
        
        if(n < 2) 
            return s;
        
        int start_idx = 0;
        int max_len = 0;
        int i = 0;
        while(i < n) {
            int l_ptr = i;
            int r_ptr = i;

            // Skip all of the duplicates
            // 
            // In the case where this set of duplicates is the largest
            // palindromic substring, then the next loop will not change any
            // of the pointers, and this set of consecutive duplicates will be counted
            // as their own palindrome.
            while(r_ptr < n - 1 && s[r_ptr] == s[r_ptr + 1]) {
                r_ptr++;
            }
            i = r_ptr + 1;
            
            // Find the largest palindrome from the middle out
            while(l_ptr > 0 && r_ptr < n - 1 && s[l_ptr - 1] == s[r_ptr + 1]) {
                l_ptr--;
                r_ptr++;
            }
            
            // Check to see if we found a new largest palindrome
            int new_len = r_ptr - l_ptr + 1;
            if(new_len > max_len) {
                max_len = new_len;
                start_idx = l_ptr;
            }   
        }
        
        return s.substr(start_idx, max_len);
    }
};
