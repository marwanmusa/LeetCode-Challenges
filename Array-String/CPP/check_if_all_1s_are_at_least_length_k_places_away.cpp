#include <vector>
using namespace std;

class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        int zeros = k;
        for (int x : nums) {
            if (x == 1) {
                if (zeros < k) {
                    return false;
                }
                zeros = 0;
            } else {
                zeros++;
            }
        }
        return true;
    }
};