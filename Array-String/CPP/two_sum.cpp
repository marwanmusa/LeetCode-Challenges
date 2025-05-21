#include <vector>
#include <unordered_map>

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

    // using one-pass hash-map
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> umap;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            int remaining_val = target - nums[i];
            if (umap.count(remaining_val) == 1) {
                return {i, umap[remaining_val]};
            }
            umap[nums[i]] = i;
        }
        return {};
    }

    // using two-pass hash-map
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> umap;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            umap[nums[i]] = i;
        }

        for (int i = 0; i < n; i++) {
            int complement = target - nums[i];
            if (umap.count(complement) == 1 && umap[complement] != i) {
                return {i, umap[complement]};
            }
        }

        return {};
    }

};