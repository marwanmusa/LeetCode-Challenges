#include <vector>
using namespace std;

class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int cur = 1, idx = 0, n = arr.size();
        while (true) {
            if (cur != arr[idx]) k--;
            if (cur == arr[idx] && idx < n-1) idx++;
            if (k == 0) break;
            cur++;
        }
        return cur;
    }

    int findKthPositive(vector<int>& arr, int k) {
        int l = 0, r = arr.size();
        while (l < r) {
            int m = l + (r - l) / 2;
            if (arr[m] - m - 1 < k) l = m + 1;
            else r = m;
        }
        return l + k;
    }
};