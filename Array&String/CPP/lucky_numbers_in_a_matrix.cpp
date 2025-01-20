#include <algorithm>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> luckyNumbers(vector<vector<int>>& matrix) {
        int c = matrix[0].size(), r = matrix.size();
        unordered_map<int, int> minr, maxc;
        for (int i = 0; i < r; i++) {
            vector<int> cur = matrix[i];
            auto smallest = min_element(cur.begin(), cur.end());
            auto it = find(cur.begin(), cur.end(), *smallest);
            minr[i] = it - cur.begin();
        }
        for (int j = 0; j < c; j++) {
            vector<int> temp;
            for (auto arr : matrix) temp.push_back(arr[j]);
            auto largest = max_element(temp.begin(), temp.end());
            auto it = find(temp.begin(), temp.end(), *largest);
            maxc[j] = it - temp.begin();
        }

        vector<int> ans;
        for (auto const [k, v] : minr) {
            if (maxc.count(v) == 1 && maxc[v] == k) ans.push_back(matrix[k][v]);
        }
        return ans;
    }

    // shorter version
    vector<int> luckyNumbers(vector<vector<int>>& matrix) {
        vector<int> res;
        for (int i = 0; i < matrix.size(); i++) {
            auto mi = min_element(matrix[i].begin(), matrix[i].end());
            int idx_min = find(matrix[i].begin(), matrix[i].end(), *mi) - matrix[i].begin();
            bool flag = true;
            for (int j = 0; j < matrix.size(); j++) {
                if (j != i && matrix[j][idx_min] > matrix[i][idx_min]) {
                    flag = false;
                    break;
                }
            }
            if (flag) res.push_back(matrix[i][idx_min]);
        }
        return res;
    }
};