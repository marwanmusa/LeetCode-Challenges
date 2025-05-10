#include <vector>
#include <algorithm>
using namespace std;

class Solution {
    public:
        int specialArray(vector<int>& nums) {
            int n = nums.size(), cnt = 0, idx = 0;
            sort(nums.begin(), nums.end());
            while (cnt < n + 1) {
                if (idx > n - 1 || cnt > n - idx) return -1;
                if (cnt <= nums[idx] && cnt == n - idx) return cnt;
                else cnt > nums[idx] ? idx++ : cnt++;
            }
            return -1;
        }

        // Binary Search approach
        int specialArray(vector<int>& nums) {
            int right = nums.size(), left = 0;
            sort(nums.begin(), nums.end());
            while (left <= right) {
                int mid = left + (right - left) / 2;
                int cnt = nums.end() - lower_bound(nums.begin(), nums.end(), mid);
                if (mid == cnt) return mid;
                else if (mid <cnt) left = mid + 1;
                else right = mid - 1;
            }
            return -1;
        }
    };
