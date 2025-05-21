#include <vector>
using namespace std;

class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        bool flat = true;
        int start = nums[0], second = nums[0], j = 0, n = nums.size();
        for (int i = 1; i < n; i++) {
            j = i;
            if (nums[i] != start) {
                second = nums[i];
                flat = false;
                break;
            }
        }
        if (flat && j == n-1) return true;
        else {
            bool inc = start < second;
            j = j+1;
            if (inc) {
                while (j < n) {
                    if (nums[j] >= second)  second = nums[j];
                    else return false;
                    j++;
                }
            } else {
                while (j < n) {
                    if (nums[j] <= second) second = nums[j];
                    else return false;
                    j++;
                }
            }
        }
    return true;
    }

    bool isMonotonic_optimized(vector<int>& nums) {
        bool increasing = true, decreasing = true;

        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] > nums[i - 1]) {
                decreasing = false;
            }
            if (nums[i] < nums[i - 1]) {
                increasing = false;
            }
        }

        return increasing || decreasing;
    }
};