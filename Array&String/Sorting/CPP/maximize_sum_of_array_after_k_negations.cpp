#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int largestSumAfterKNegations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        for (int i = 0; i < k; i++) {
            nums[i] = -nums[i];
        }
        return accumulate(nums.begin(), nums.end(), 0);
    }
};