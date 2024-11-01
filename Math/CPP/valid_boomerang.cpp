#include <cmath>
#include <vector>
using namespace std;

class Solution {
public:
    bool isBoomerang(vector<vector<int>>& pos) {
        return 0.5 * abs(pos[0][0] * (pos[1][1] - pos[2][1]) + pos[1][0] * (pos[2][1] - pos[0][1]) + pos[2][0] * (pos[0][1] - pos[1][1])) > 0;
    }
};