#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> ans;
        for (int j = 0; j < n; j++) {
            vector<int> cur;
            for (int i = 0; i < m; i++) {
                cur.push_back(matrix[i][j]);
            }
            ans.push_back(cur);
        }
        return ans;
    }
};