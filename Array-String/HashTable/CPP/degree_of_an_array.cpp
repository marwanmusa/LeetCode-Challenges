#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        unordered_map<int, int> freq;
        unordered_map<int, int> firstIdx;
        unordered_map<int, int> lastIdx;

        for (int i = 0; i < nums.size(); ++i) {
            int x = nums[i];
            freq[x]++;
            if (!firstIdx.count(x)) firstIdx[x] = i;
            lastIdx[x] = i;
        }

        int degree = 0;
        int minLen = nums.size();

        for (const auto& [num, count] : freq) {
            if (count > degree) {
                degree = count;
                minLen = lastIdx[num] - firstIdx[num] + 1;
            } else if (count == degree) {
                minLen = min(minLen, lastIdx[num] - firstIdx[num] + 1);
            }
        }

        return minLen;
    }
};
