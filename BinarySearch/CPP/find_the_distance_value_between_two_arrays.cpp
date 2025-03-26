#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;
class Solution {
public:
    int findTheDistanceValue(vector<int>& arr1, vector<int>& arr2, int d) {
        sort(arr2.begin(), arr2.end());
        int i = 0, j = 0, m = arr1.size(), n = arr2.size(), res = 0;
        for (int x : arr1) {
            int l = 0, r = n-1;
            bool hasclosevalue = false;
            while( l <= r) {
                int mid = l + (r-l) / 2, cur = arr2[mid];
                if (abs(cur - x) <= d) {
                    hasclosevalue = true;
                    break;
                }
                else if (cur < x) l = mid + 1;
                else r = mid - 1;
            }
            if (!hasclosevalue) res++;
        }
        return res;
    }
};