#include <vector>
using namespace std;

class Solution {
public:
    vector<int> sumZero(int n) {
        int mid = n / 2;
        vector<int> res;
        for (int i = -mid; i < mid + 1; i++) {
            if (i == 0 && n % 2 == 0) continue;
            else res.push_back(i);
        }
        return res;
    }
};