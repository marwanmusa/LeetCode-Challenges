#include <format>
#include <iostream>
#include <string>
using namespace std;

class Solution {
    public:
        string thousandSeparator(int n) {
            if (n < 1000) return to_string(n);
            string nstr = to_string(n);
            int le = nstr.size();
            int rem = le % 3;
            string sliced = nstr.substr(rem), ans = "";
            int sliced_len = sliced.size();
            for (int i = 0; i < sliced_len; i += 3) {
                ans += format(".{}", sliced.substr(i, 3));
            }
            return rem > 0? nstr.substr(0, rem) + ans : ans.substr(1);
        }

        // shorter
        string thousandSeparator(int n) {
            string s = to_string(n), res;
            int len = s.size();
            for (int i = 0; i < len; ++i) {
                if (i > 0 && (len - i) % 3 == 0) res += '.';
                res += s[i];
            }
            return res;
        }
    };