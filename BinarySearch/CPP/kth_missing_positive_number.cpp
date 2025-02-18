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
};