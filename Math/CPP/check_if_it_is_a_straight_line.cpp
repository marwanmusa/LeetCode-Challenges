#include <vector>
using namespace std;

class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        if (coordinates.size() == 2) return true;
        int xs = coordinates[1][0] - coordinates[0][0];
        int ys = coordinates[1][1] - coordinates[0][1];
        for (int i = 2; i < coordinates.size(); i++) {
            int curxs = coordinates[i][0] - coordinates[i-1][0];
            int curys = coordinates[i][1] - coordinates[i-1][1];
            if (xs * curys != ys * curxs) return false;
        }
        return true;
    }
};