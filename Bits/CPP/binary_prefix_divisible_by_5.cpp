#include <vector>
using namespace std;

class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& nums) {
        int cur = nums[0];
        vector<bool> res;
        res.push_back(nums[0] == 0);
        for (int i = 1; i < nums.size(); i++) {
            cur = (cur * 2 + nums[i]) % 5 ;
            res.push_back(cur == 0);
        }
        return res;
    }
};