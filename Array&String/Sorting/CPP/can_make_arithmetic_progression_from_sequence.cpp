#include <algorithm>
#include <vector>
using namespace std;

class Solution {
    public:
        bool canMakeArithmeticProgression(vector<int>& arr) {
            sort(arr.begin(), arr.end());
            int diff = arr[1] - arr[0], n = arr.size();
            if (n == 2) return true;
            for (int i = 2; i < n; i++){
                if (arr[i] - arr[i-1] != diff) return false;
            }
            return true;
        }
    };