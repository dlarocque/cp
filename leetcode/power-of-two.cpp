class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n <= 0) {
            return false;
        }
        // only one bit if power of two
        bool hit = false;
        for (int i = 0; i < 32; i++) {
            if (n & (1 << i)) {
                if (hit) {
                    return false;
                } else {
                    hit = true;
                }
            }
        }

        return true;
    }
};