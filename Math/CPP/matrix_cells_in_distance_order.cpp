#include <map>
#include <cmath>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        map<int, vector<vector<int>>> hmap;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                vector<int> pos{i, j};
                hmap[dist(pos, rCenter, cCenter)].push_back(pos);
            }
        }

        vector<vector<int>> res;
        for (auto& [distance, cells] : hmap) {
            res.insert(res.end(), cells.begin(), cells.end());
        }

        return res;
    }

private:
    int dist(const vector<int>& pos, int rCenter, int cCenter) {
        return abs(pos[0] - rCenter) + abs(pos[1] - cCenter);
    }
};