#include <cmath>
#include <vector>
using namespace std;

class Solution {
public:
    int maximum69Number (int num) {
        vector<int> nums;
        while (num > 0) {
            int rem = num % 10;
            num /= 10;
            nums.insert(nums.begin(), rem);
        }
        bool flip = false;
        int pows = nums.size() - 1, ans = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 9 && !flip) {
                nums[i] = 9;
                flip = true;
            }
            ans += nums[i] * pow(10, pows);
            pows -= 1;
        }
        return ans;
    }
};