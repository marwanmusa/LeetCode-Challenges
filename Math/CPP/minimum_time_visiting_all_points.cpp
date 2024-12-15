#include <cmath>
#include <vector>
using namespace std;

class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int n = points.size(), res = 0;
        if (n == 1) return 0;
    for (int i = 0; i < points.size() - 1; i++) {
            int a = points[i][0], b = points[i][1],
                c = points[i+1][0], d = points[i+1][1],
                shortDistanceXY = min(abs(a-c), abs(b-d)),
                longDistannceXY = max(abs(a-c), abs(b-d));
            res += shortDistanceXY + (longDistannceXY - shortDistanceXY);
        }
        return res;
    }
};