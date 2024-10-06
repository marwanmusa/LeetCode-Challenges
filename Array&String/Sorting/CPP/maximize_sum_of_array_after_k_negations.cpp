#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

class Solution {
public:
    int largestSumAfterKNegations(vector<int>& nums, int k) {
        vector<int> negs;
        for (int x: nums) {
            if (x < 0) negs.push_back(x);
        }
        sort(negs.begin(), negs.end());

        return accumulate(nums.begin(), nums.end(), 0);
    }
};