#include <set>

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> rows = vector<unordered_set<char>>(9);
        vector<unordered_set<char>> cols = vector<unordered_set<char>>(9);
        vector<unordered_set<char>> boxes = vector<unordered_set<char>>(9);
        
        for (int i = 0 ; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char c = board[i][j];
                if (c == '.') {
                    continue;
                }
                int box = (i / 3) * 3 + (j / 3);
                // Check if valid
                if (rows[i].find(c) != rows[i].end() ||
                    cols[j].find(c) != cols[j].end() || 
                    boxes[box].find(c) != boxes[box].end()) {
                    return false;
                }
                
                rows[i].insert(c);
                cols[j].insert(c);
                boxes[box].insert(c);
            }
        }
        
        return true;
    }
};
