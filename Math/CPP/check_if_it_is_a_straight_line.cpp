#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        if (coordinates.size() == 2) return true;
        int xs = abs(coordinates[0][0] - coordinates[1][0]);
        int ys = abs(coordinates[0][1] - coordinates[1][1]);
        for (int i = 1; i < coordinates.size(); i++) {
            if (abs(coordinates[i][0] - coordinates[i-1][0]) != xs || abs(coordinates[i][1] - coordinates[i-1][1]) != ys) return false;
        }
        return true;
    }
};