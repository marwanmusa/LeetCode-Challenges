#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<vector<int>> largeGroupPositions(string s) {
        int start = 0, end = 0, max = 2;
        vector<vector<int>> maxIdx;
        char cur = s[0];
        for (int i = 0; i < s.size(); i++) {
            if (s[i] != cur) {
                if (end-start >= max) maxIdx.push_back(vector<int>{start, end});
                end = start = i;
                cur = s[i];
                continue;
            } end = i;
        }
        if (start != end && end - start >= max) maxIdx.push_back(vector<int>{start, end});
        return maxIdx;
    }
};