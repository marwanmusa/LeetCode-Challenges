#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int maxc = *max_element(candies.begin(), candies.end()), n = candies.size();
        vector<bool> res(n);
        for (int i = 0; i < n; i++) {
            res[i] = candies[i] + extraCandies >= maxc;
        }
        return res;
    }
};