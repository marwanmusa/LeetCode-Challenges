#include <string>
#include <unordered_map>
#include <cmath>
using namespace std;

class Solution {
public:
    int maxNumberOfBalloons(string text) {
        unordered_map<char, int> word;
        for (char const& k: text) {
            word[k]++;
        }
        int res = text.size();
        unordered_map<char, int> balloon = {{'b', 1}, {'a', 1}, {'l', 2}, {'o', 2}, {'n', 1}};
        for (auto const& [w, value]: balloon) {
            if (word.count(w) == 0) return 0;
            res = min(res, word.at(w) / value);
        }
        return res;
    }
};