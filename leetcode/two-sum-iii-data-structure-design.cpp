#include <vector>
#include <unordered_map>

using namespace std;

class TwoSum {
public:
    TwoSum() {
    }

    void add(int number) {
        m[number]++;
    }

    bool find(int value) {
        for (const auto& [num, cnt] : m) {
            int target = value - num;
            if (num != target) {
                if (m.count(target)) {
                    return true;
                }
            } else if (cnt > 1) {
                return true;
            }
        }
        return false;
    }

private:
    unordered_map<int, int> m;
};