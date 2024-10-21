# include <numeric>
# include <vector>
using namespace std;

class Solution {
public:
    bool canThreePartsEqualSum(vector<int>& arr) {
        int sums = accumulate(arr.begin(), arr.end(), 0), n = arr.size();
        int mod = sums % 3, rem = sums / 3, parts = 3, cur = 0;
        if (mod) return false;
        for (int i = 0; i < n; i++) {
            cur += arr[i];
            if (parts == 1 && i < n - 1) continue;
            if (cur == rem) {
                cur = 0;
                parts--;
            }
        }
        return parts == 0;
    }

    // Shorter
    bool canThreePartsEqualSum(vector<int>& A) {
        int sum = accumulate(A.begin(), A.end(), 0), part = 0, average = sum / 3, cnt = 0;
        for (int a : A) {
            part += a;
            if (part == average) { // find the average: sum / 3
                ++cnt; // find an average, increase the counter.
                part = 0; // reset part.
            }
        }
        return cnt >= 3 && sum % 3 == 0;
    }
};