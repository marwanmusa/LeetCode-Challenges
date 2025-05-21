#include <algorithm>
#include <numeric>
#include <vector>
using namespace std;

class Solution {
    public:
        double trimMean(vector<int>& arr) {
            sort(arr.begin(), arr.end());
            double n = arr.size();
            double cut = n / 20;
            double sum = accumulate(arr.begin() + cut, arr.end() - cut, 0);
            return sum / (n - (2 * cut));
        }
    };