#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        int len = nums.size() / 2, res = 0;
        map<int, int> cnt;
        for (int n : nums) {
            cnt[n] += 1;
            if (cnt[n] == len) {
                res = n;
                break;
            }
        }
        return res;
    }

    int repeatedNTimes(vector<int>& nums) {
        int freq[10001];
        for (int i = 0; i < 10001; i++)
            freq[i] = 0;
        for (int num: nums)
            if (++freq[num] == nums.size() / 2)
                return num;
        return -1;
    }
};