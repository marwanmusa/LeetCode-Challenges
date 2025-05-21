#include <algorithm>
#include <vector>
using namespace std;

class Solution {
    public:
        bool threeConsecutiveOdds(vector<int>& arr) {
            int n = arr.size();
            if ( n < 3) return false;
            for (int i = 0; i < n - 2; i++) {
                if (all_of(arr.begin() + i, arr.begin() + i + 3, [](int x) {
                    return x & 1;
                })) return true;
            }
            return false;
        }
    };