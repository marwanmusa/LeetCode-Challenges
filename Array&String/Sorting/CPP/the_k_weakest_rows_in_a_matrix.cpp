#include <algorithm>
#include <numeric>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        vector<pair<int, int>> weak_rank;
        for (int i = 0; i < mat.size(); i++) {
            int soldier_sum = accumulate(mat[i].begin(), mat[i].end(), 0);
            weak_rank.push_back({soldier_sum, i});
        }
        sort(weak_rank.begin(), weak_rank.end());

        vector<int> res;
        for (int i = 0; i < k; i++) res.push_back(weak_rank[i].second);
        return res;
    }
};