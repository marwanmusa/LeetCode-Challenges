#include <vector>
#include <algorithm>
using namespace std;

class Solution {
    public:
        bool isCovered(std::vector<std::vector<int>>& ranges, int left, int right) {
            // Use a simple array instead of std::map since keys are continuous and small
            std::vector<bool> covered(right - left + 1, false);

            for (const auto& r : ranges) {
                int start = std::max(left, r[0]);
                int end = std::min(right, r[1]);
                for (int i = start; i <= end; ++i) {
                    covered[i - left] = true;  // shift index to 0-based
                }
            }

            for (bool c : covered) {
                if (!c) return false;
            }
            return true;
        }
    };
