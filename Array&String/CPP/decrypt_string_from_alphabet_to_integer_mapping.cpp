#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    string freqAlphabets(string s) {
        unordered_map<string, int> mp;
        string cres = "#";
        string ans;
        for (int i = 1; i < 27; i++) {
            mp[to_string(i)] = char(i+96);
        }
        for (int i = 10; i < 27; i++) {
            mp[to_string(i)+cres] = mp[to_string(i)];
            mp.erase(to_string(i));
        }
        int i = 0, n = s.size();
        while (i < n - 2) {
            if (s[i+2] != '#') {
                ans.push_back(mp[s.substr(i, 1)]);
                i += 1;
            } else {
                ans.push_back(mp[s.substr(i, 3)]);
                i += 3;
            }
        }
        if (i <= n-1) {
            for (int j = i; j < n; j++) ans.push_back(mp[s.substr(j)]);
        }
        return ans;
    }
};