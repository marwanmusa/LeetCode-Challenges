#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    // O(1) space solution
    vector<int> findErrorNums(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int duplicate = -1, missing = -1, i = 1, prev = -1;
        for (int num : nums) {
            if (prev == num) {
                duplicate = num;
            }
            prev = num;
            if (i == num) i++;
        }
        return {duplicate, i};
    }

    // O(n) space solution
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        vector<int> count(n + 1, 0);
        for (int num : nums) {
            count[num]++;
        }

        int duplicate = -1, missing = -1;
        for (int i = 1; i <= n; ++i) {
            if (count[i] == 0) missing = i;
            else if (count[i] == 2) duplicate = i;
        }

        return {duplicate, missing};
    }

    // O(1) space solution but without sorting
    vector<int> findErrorNums(vector<int>& nums) {
        int duplicate = -1, missing = -1;

        // First pass: mark visited numbers
        for (int num : nums) {
            int index = abs(num) - 1;
            if (nums[index] < 0) {
                duplicate = abs(num);
            } else {
                nums[index] *= -1;
            }
        }

        // Second pass: find the missing number
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] > 0) {
                missing = i + 1;
                break;
            }
        }

        return {duplicate, missing};
    }
};