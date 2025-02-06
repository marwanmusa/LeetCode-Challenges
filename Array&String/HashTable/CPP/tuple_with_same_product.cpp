#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

static const int _ = []() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    return 0;
}();

class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        unordered_map<long long, int> mult;
        int res = 0;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i+1; j < nums.size(); j++) {
                long long m = nums[i] * nums[j];
                mult[m]++;
            }
        }
        for (auto const& [k, v] : mult) {
            if (v >= 2) res += comb(v, 2) * 8;
        }
        return res;
    }

    long long comb(int n, int k) {
        if (k > n - k) k = n - k;
        long long res = 1;
        for (int i = 0; i < k; ++i) {
            res = res * (n - i) / (i + 1);
        }
        return res;
    }

    // without using comb
    int tupleSameProduct(vector<int>& nums) {
        unordered_map<long long, int> mult;
        int res = 0;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i+1; j < nums.size(); j++) {
                long long m = nums[i] * nums[j];
                mult[m]++;
            }
        }
        for (auto const& [k, v] : mult) {
            if (v >= 2) res += v * (v-1) * 4;
        }
        return res;
    }
};