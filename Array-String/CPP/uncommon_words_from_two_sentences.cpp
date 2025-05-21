#include <map>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        istringstream s(s1 + " " + s2);
        map<string, int> cs;
        while (s >> s1) cs[s1]++;
        vector<string> res;
        for (auto& k: cs) {
            if (k.second == 1 ) res.push_back(k.first);
        }
        return res;
    }
};