#include <cmath>
#include <vector>
using namespace std;

// Solution 1: Using bitwise operations

class Solution {
public:
    int bitwiseComplement(int n) {
        if (n == 0) return 1;
        vector<int> bins;
        while (n > 0) {
            bins.push_back(abs((n % 2) - 1));
            n /= 2;
        }
        int res = 0;
        for (int i = 0; i < bins.size(); i++) {
            res += bins[i] * pow(2, i);
        }
        return res;
    }

    // using shift operator
    int bitwiseComplement(int n) {
        if (n == 0) return 1;
        vector<int> bins;
        while (n > 0) {
            bins.insert(bins.begin(), abs((n % 2) - 1));
            n /= 2;
        }
        int res = 0;
        for (int i : bins) {
            res = (res << 1) | i;
        }
        return res;
    }

    // shorter
    int bitwiseComplement(int N) {
        int mask = 1;

        while (mask < N)
        mask = (mask << 1) + 1;

        return mask ^ N;
    }
};