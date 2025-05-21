#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        unordered_map<char, int> temp = counter(words[0]);
        for (int i = 1; i < words.size(); i++) {
            unordered_map<char, int> cur = counter(words[i]);
            unordered_map<char, int> calc;
            for (char w : intersect(cur, temp)) calc[w] = min(cur[w], temp[w]);
            temp = calc;
        }
        vector<string> ans;
        for (auto k : temp) {
            for (int i = 0; i < k.second; i++) ans.push_back(string {k.first});
        }
        return ans;
    }

    unordered_map<char, int> counter(string& word) {
        unordered_map<char, int> map;
        for (char w : word) map[w] += 1;
        return map;
    }

    vector<char> intersect(unordered_map<char, int>& map1, unordered_map<char, int>& map2) {
        vector<char> res;
        for (auto k: map1) {
            if (map2.find(k.first) != map2.end()) res.push_back(k.first);
        }
        return res;
    }
};