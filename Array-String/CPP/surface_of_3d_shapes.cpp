#include <vector>
using namespace std;

class Solution {
public:
    int surfaceArea(vector<vector<int>>& grid) {
        int ans = 0, m = grid.size(), n = grid[0].size();
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j]) ans += 4 * grid[i][j] + 2;
                if (i) ans -= min(grid[i][j], grid[i - 1][j]);
                if (i+1 < m) ans -= min(grid[i][j], grid[i + 1][j]);
                if (j) ans -= min(grid[i][j], grid[i][j - 1]);
                if (j+1 < n) ans -= min(grid[i][j], grid[i][j + 1]);
            }
        }
        return ans;
    }
};