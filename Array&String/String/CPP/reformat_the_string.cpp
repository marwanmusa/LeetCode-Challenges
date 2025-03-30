#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string reformat(string s) {
        string digit = "", alpha = "", ans = "";

        for (char x : s) isdigit(x) ? digit += x : alpha += x;

        int p = digit.size(), q = alpha.size();
        if (abs(p - q) > 1) return "";

        if (p < q) {
            swap(digit, alpha);
            swap(p, q);
        }

        ans.reserve(s.size());

        for (size_t  i = 0; i < q; ++i) {
            ans.push_back(digit[i]);
            ans.push_back(alpha[i]);
        }

        if (p > q) {
            ans.push_back(digit[q]);
        }

        return ans;
    }
};

int main() {
    Solution solution;
    string s = "a0b1c2";
    cout << solution.reformat(s) << endl;
    return 0;
}