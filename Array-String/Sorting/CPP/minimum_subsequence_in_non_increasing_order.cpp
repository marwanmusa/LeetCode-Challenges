#include <vector>
#include <numeric>
#include <functional>
using namespace std;

class Solution {
public:
    vector<int> minSubsequence(vector<int>& nums) {
        if (nums.size() == 1) return nums;
        sort(nums.begin(), nums.end(), greater<>());
        int total = accumulate(nums.begin(), nums.end(), 0);
        int l = nums[0];
        vector<int> res{nums[0]};
        for (int i = 1; i < nums.size(); i++) {
            if (l > total - l) break;
            l += nums[i];
            res.push_back(nums[i]);
        }
        return res;
    }
};