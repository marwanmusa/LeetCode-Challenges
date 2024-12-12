#include <vector>
using namespace std;

template<typename T>
vector<T> flatten(const std::vector<std::vector<T>> &orig)
{
    std::vector<T> ret;
    for(const auto &v: orig)
        ret.insert(ret.end(), v.begin(), v.end());
    return ret;
}

class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        int r = grid.size(), c = grid[0].size();
        vector<int> flattened = flatten(grid);

        // Shift the flattened vector
        int n = flattened.size();
        k %= n;
        rotate(flattened.begin(), flattened.begin() + n - k, flattened.end());

        // Reshape the flattened vector back to a 2D matrix
        vector<vector<int>> res;
        for (int i = 0; i < r; ++i) {
            res.push_back(vector<int>(flattened.begin() + i * c, flattened.begin() + (i + 1) * c));
        }
        return res;
    }
};