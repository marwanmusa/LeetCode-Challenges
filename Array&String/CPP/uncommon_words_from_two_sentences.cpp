#include <map>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        s1 += ' ';
        s2 += ' ';
        string temp;
        map<string, int> cs1, cs2;
        vector<string> res;
        addToCounter(s1, cs1);
        addToCounter(s2, cs2);
        countRes(cs1, cs2, res);
        countRes(cs2, cs1, res);
        return res;
    }

    void addToCounter(string& s, map<string, int>& counter) {
        string temp;
        for (char e: s) {
            if (e == ' ') {
                counter[temp] += 1;
                temp = "";
            } else {
                temp.push_back(e);
            }
        }
    }

    void countRes(map<string, int>& counter1, map<string, int>& counter2, vector<string>& res) {
        for (auto& k: counter1) {
            if (k.second == 1 && counter2.find(k.first) == counter2.end()) res.push_back(k.first);
        }
    }
};