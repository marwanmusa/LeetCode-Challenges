#include <algorithm>
#include <vector>
using namespace std;


bool comp(int a, int b) {
    if (__builtin_popcount(a) == __builtin_popcount(b))
        return a < b;
    return __builtin_popcount(a) < __builtin_popcount(b);
}


class Solution {
public:
    vector<int> sortByBits(vector<int>& arr) {
        vector<pair<int, int>> bitsets;
        for (int x : arr) {
            bitsets.push_back({countBits(x), x});
        }
        sort(bitsets.begin(), bitsets.end());
        vector<int> res;
        for (auto bit : bitsets) res.push_back(bit.second);
        return res;
    }

    int countBits(int n) {
        int res = 0;
        while(n > 0) {
            res += (n & 0x1);
            n >>= 1;
        }
        return res;
    }

    // Use built-in function
    vector<int> sortByBits(vector<int>& arr) {
        vector<pair<int, int>> bitsets;
        for (int x : arr) {
            bitsets.push_back({__builtin_popcount(x), x});
        }
        sort(bitsets.begin(), bitsets.end());
        vector<int> res;
        for (auto bit : bitsets) res.push_back(bit.second);
        return res;
    }

    // using the original array
    vector<int> sortByBits(vector<int>& arr) {
        sort(arr.begin(), arr.end(), comp);
        return arr;
    }
};