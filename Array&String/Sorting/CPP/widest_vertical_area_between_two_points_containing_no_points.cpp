#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        vector<int> xs;
        for (const auto point : points) xs.push_back(point[0]);
        sort(xs.begin(), xs.end());

        int n = points.size(), res = 0;
        for (int i = 1; i < n; i++) {
            res = max(res, xs[i] - xs[i-1]);
        }
        return res;
    }

    // with custom sort function
    static bool compare(vector<int>& a, vector<int>& b) {
        return a[0] < b[0];
    }

    int maxWidthOfVerticalArea2(vector<vector<int>>& points) {
        sort(points.begin(), points.end(), compare);
        int n = points.size(), res = 0;
        for (int i = 1; i < n; i++) {
            res = max(res, points[i][0] - points[i-1][0]);
        }
        return res;
    }
};