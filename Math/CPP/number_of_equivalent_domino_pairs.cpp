#include <cmath>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        unordered_map<int, int> umap;
        for (vector<int>& dom : dominoes) {
            int key = min(dom[0], dom[1]) * 10 + max(dom[0], dom[1]);
            umap[key]++;
        }

        int res = 0;
        for (auto p: umap) {
            if (p.second > 1) res += (p.second * (p.second - 1) / 2);
        }
        return res;
    }
};