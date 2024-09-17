#include <algorithm>
#include <vector>
using namespace std;

// 976. Largest Perimeter of a Triangle

class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        int ans = 0;
        sort(nums.begin(), nums.end());
        for (int i = nums.size() - 1; i - 2 >= 0; i--) {
            int a = nums[i], b = nums[i-1], c = nums[i-2];
            if (check(a,b,c)) ans = max(ans, a+b+c);
        }
        return ans;
    }

    bool check(int a, int b, int c) {
        return ((a + b) > c) && ((a + c) > b) && ((b + c) > a);
    }
};