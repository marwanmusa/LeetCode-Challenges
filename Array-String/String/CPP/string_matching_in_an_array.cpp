#include <algorithm>
#include <string>
#include <vector>
using namespace std;

bool comp(string a, string b) {
    return a.size() < b.size();
}

class Solution {
public:
    vector<string> stringMatching(vector<string>& words) {
        vector<string> res;
        sort(words.begin(), words.end(), comp);
        for (int i = 0; i < words.size(); i++) {
            for (int j = i+1; j < words.size(); j++) {
                if (words[j].find(words[i]) != -1) {
                    res.push_back(words[i]);
                    break;
                }
            }
        }
        return res;
    }
};