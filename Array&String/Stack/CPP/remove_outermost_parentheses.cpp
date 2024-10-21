#include <string>
using namespace std;

class Solution {
public:
    string removeOuterParentheses(string s) {
        int l = 0, r = 0, idx = 0, n = s.size();
        string res = "";

        for (int i = 0; i < n; i++) {
            if (s[i] == '(') l++;
            else r++;

            if (l == r) {
                res += s.substr(idx + 1, (i - (idx + 1)));
                idx = i + 1;
                l = 0;
                r = 0;
            }
        }
        return res;
    }
};