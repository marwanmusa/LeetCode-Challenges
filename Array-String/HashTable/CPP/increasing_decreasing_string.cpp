#include <algorithm>
#include <map>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string sortString(string s) {
        map<char, int> cnt;
        for (char w: s) cnt[w]++;

        string res = "";
        int n = s.size();
        bool increasing = true;
        while (n > 0) {
            string cur = "";
            for (auto it = cnt.begin(); it != cnt.end(); ++it) {
                if (it->second == 0) {
                    continue;
                }
                cur += it->first;
                it->second--;
                n--;
            }
            if (!increasing) reverse(cur.begin(), cur.end());
            res += cur;
            increasing = !increasing;
        }
        return res;
    }

    string sortString(string s) {
        // Count the occurrences of each character
        vector<int> cnt(26, 0);
        for (char ch : s) {
            cnt[ch - 'a']++;
        }

        string result;
        int remaining = s.size();

        // Continue until all characters are used
        while (remaining > 0) {
            for (int i = 0; i < 26; i++) {
                if (cnt[i] > 0) {
                    result += ('a' + i);
                    cnt[i]--;
                    remaining--;
                }
            }
            // Append characters in decreasing order
            for (int i = 25; i >= 0; i--) {
                if (cnt[i] > 0) {
                    result += ('a' + i);
                    cnt[i]--;
                    remaining--;
                }
            }
        }
        return result;
    }

};