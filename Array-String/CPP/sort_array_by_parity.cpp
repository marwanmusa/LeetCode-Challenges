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
    return nums;
    }
};