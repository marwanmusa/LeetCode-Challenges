#include <algorithm>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int minCostToMoveChips(vector<int>& position) {
        int odd = 0, even = 0;
        unordered_map<int, int> counter;
        for (const int n: position) counter[n]++;
        for (const auto [k, v] : counter) {
            if (k % 2 == 0) even += v;
            else odd += v;
        }
        return min(odd, even);
    }
};