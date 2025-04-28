#include <string>

using namespace std;

class Solution {
    public:
        string modifyString(string s) {
            int n = s.size(), i = 0;
            if (n == 1 && s == "?") return "a";
            for (i; i < n; i++) {
                if (s[i] == '?') {
                    int l = i <= 0 ? -1 : s[i-1] - 'a',
                        r = i > n ? -1 : s[i+1] - 'a',
                        cur = 0;
                    while (cur < 26) {
                        if (cur != l && cur != r) break;
                        cur++;
                    }
                    s[i] = (char)cur+97;
                }
            }
            return s;
        }

        // cleaner solution
        string modifyString(string s) {
            int n = s.size();
            if (n == 1 && s == "?") return "a";
            for (int i = 0; i < n; i++) {
                if (s[i] == '?') {
                    for (char c = 'a'; c <= 'z'; c++) {
                        if ((i > 0 && s[i-1] == c) || (i < n-1 && s[i+1] == c)) continue;
                        s[i] = c;
                        break;
                    }
                }
            }
            return s;
        }
    };