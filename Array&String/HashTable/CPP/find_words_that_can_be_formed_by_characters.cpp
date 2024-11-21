#include <unordered_map>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        unordered_map<char, int> cntChars = cnt(chars);
        int res = 0;
        for (const string w: words) {
            unordered_map<char, int> cur = cnt(w);
            res += w.size();
            for (auto p: cur) {
                if (cntChars.count(p.first) == 0 || p.second > cntChars.at(p.first)) {
                    res -= w.size();
                    break;
                }
            }
        }
        return res;
    }

    unordered_map<char, int> cnt(string word) {
        unordered_map<char, int> res;
        for (char c: word) res[c]++;
        return res;
    }
};