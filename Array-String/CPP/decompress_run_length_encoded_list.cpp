#include <vector>
using namespace std;

class Solution {
public:
    vector<int> decompressRLElist(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans;
        for (int i = 0; i < n-1; i += 2) {
            int freq = nums[i], val = nums[i+1];
            for (int j = 0; j < freq; j++) {
                ans.push_back(val);
            }
        }
        return ans;
    }
};