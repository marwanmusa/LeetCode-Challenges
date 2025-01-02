#include <vector>
using namespace std;

class Solution {
public:
    vector<int> getNoZeroIntegers(int n) {
        for (int i = 1; i < n; i++) {
            if (isNoZero(i) && isNoZero(n-i)) return vector<int>{i, n-i};
        }
        return vector<int>{};
    }
    bool isNoZero(int n) {
        while (n > 0) {
            if (!(n & 0x1)) {
                int nNext = n / 10;
                if (n - (10 * nNext) == 0) return false;
            }
            n /= 10;
        }
        return true;
    }
};