#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
public:
    string reformat(string s) {
        string digit = "", alpha = "", ans = "";

        for (char x : s) {
            if (isdigit(x)) digit += x;
            else alpha += x;
        }

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