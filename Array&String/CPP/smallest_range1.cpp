#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int smallestRangeI(vector<int>& nums, int k) {
        return max(*max_element(nums.begin(), nums.end()) - *min_element(nums.begin(), nums.end()) - 2*k, 0);
    }
};