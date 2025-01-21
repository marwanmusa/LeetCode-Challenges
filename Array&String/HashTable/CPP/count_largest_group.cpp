#include <algorithm>
#include <map>
using namespace std;

class Solution {
public:
    int countLargestGroup(int n) {
        map<int, int> digitGroup;
        int maxd = 0, ans = 0;
        for (int i = 1; i < n+1; i++) {
            int sumDigits = 0;
            int cur = i;
            while (cur > 0) {
                sumDigits += cur % 10;
                cur /= 10;
            }
            digitGroup[sumDigits]++;
            maxd = max(maxd, digitGroup[sumDigits]);
        }
        for (auto it = digitGroup.begin(); it != digitGroup.end(); ++it) {
            if (it->second == maxd) ans++;
        }
        return ans;
    }
};