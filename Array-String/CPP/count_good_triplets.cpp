#include <algorithm>
#include <vector>
using namespace std;

class Solution {
    public:
        int countGoodTriplets(vector<int>& arr, int a, int b, int c) {
            int cnt = 0, n = arr.size();
            for (int i = 0; i < n - 2; i++) {
                for (int j = i + 1; j < n - 1; j++) {
                    int a_ = abs(arr[i] - arr[j]);
                    if (a < a_) continue;
                    for (int k = j + 1; k < n; k++) {
                        int b_ = abs(arr[j] - arr[k]), c_ = abs(arr[i] - arr[k]);
                        if (b < b_ || c < c_) continue;
                        if (a_ <= a && b_ <= b && c_ <= c) cnt++;
                    }
                }
            }
            return cnt;
        }
    };