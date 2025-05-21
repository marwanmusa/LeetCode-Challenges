#include <algorithm>
#include <limits>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int roof = numeric_limits<int>::max();
        vector<vector<int>> res;
        for (int i = 0; i < arr.size() - 1; i++) {
            int diff = arr[i+1] - arr[i];
            if (diff < roof) {
                roof = diff;
                res.clear();
            } else if (diff > roof) continue;
            res.push_back(vector<int>{{arr[i], arr[i+1]}});
        }
        return res;
    }
};