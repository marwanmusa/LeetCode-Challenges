#include <algorithm>
#include <numeric>
#include <vector>

using namespace std;

class Solution {
public:
    int largestSumAfterKNegations(vector<int>& nums, int k) {
        vector<int> ans, pos;
        for (int x : nums) {
            if (x < 0) ans.push_back(x);
        }
        sort(ans.begin(), ans.end());
        for (int x : nums) {
            if (x >= 0) pos.push_back(x);
        }
        int n = ans.size();
        for (int i = 0; i < min(k, n); i++) {
            ans[i] = -ans[i];
        }
        k -= min(k, n);
        ans.reserve(ans.size() + pos.size());
        ans.insert(ans.end(), pos.begin(), pos.end());
        sort(ans.begin(), ans.end());
        if (k && k % 2)  ans[0] = -ans[0];
        return accumulate(ans.begin(), ans.end(), 0);
    }

    // shorter
    int largestSumAfterKNegations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        for (int i = 0; k > 0 && i < nums.size() && nums[i] < 0; ++i, --k) {
            nums[i] = -nums[i];
        }
        return accumulate(nums.begin(), nums.end(), 0) - ((k % 2) * *min_element(nums.begin(), nums.end()) * 2);
    }
};