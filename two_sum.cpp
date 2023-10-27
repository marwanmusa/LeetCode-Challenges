#include <vector>

class Solution {
public:
    // Brute Force
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {}; // No solution found
    }

    // using set
    vector<int> twoSum(vector<int>& nums, int target) {
        
    }

};