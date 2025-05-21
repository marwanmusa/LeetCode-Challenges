#include <map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        map<int, int> cnt;
        for (int x: nums) {
            cnt[x]++;
        }
        auto it = cnt.begin();
        int prev = it->second;
        if (it != cnt.end()) ++it;
        cnt.begin()->second = 0;
        for (; it != cnt.end(); ++it) {
            int cur = it->second;
            it->second = prev;
            prev += cur;
        }
        vector<int> res;
        for (int x : nums) res.push_back(cnt[x]);
        return res;
    }
};