#include <vector>
using namespace std;

class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& nums) {
        if (nums.size() <= 1) return nums;
        int i = 0;
        for (int j = 0; j < nums.size(); j++) {
            if (nums[j] % 2 == 0) {
                int temp = nums[j];
                nums[j] = nums[i];
                nums[i] = temp;
                i++;
            }
        }

        int j = 1;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] % 2 == 1) {
                int temp = nums[j];
                nums[j] = nums[i];
                nums[i] = temp;
                j += 2;
            }
        }
    return nums;
    }

    // method 2
    vector<int> sortArrayByParityII(vector<int>& nums) {
        int i = 0, j = 1, n = nums.size();
        while (i < n && j < n) {
            if (nums[i] % 2 == 0) i += 2;
            else if (nums[j] % 2 == 1) j += 2;
            else swap(nums[i], nums[j]);
        }
        return nums;
    }
};