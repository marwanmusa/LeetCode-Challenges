#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minStartValue(vector<int>& nums) {
        int l{}, s{};
        for (int x : nums) {
            s += x;
            l = min(l, s);
        }
        return 1 - l;
    }
};