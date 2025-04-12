#include <string>
#include <cmath>

using namespace std;

class Solution {
public:
    string makeGood(string s) {
        string ans;
        ans += s[0];
        int n = s.size();
        for (int i = 1; i < n; i++) {
            char cur = s[i];
            if (!ans.empty() && abs(static_cast<int>(ans.back()) - static_cast<int>(cur)) == 32) {
                ans.pop_back();
                continue;
            }
            ans += cur;
        }
        return ans;
    }
};