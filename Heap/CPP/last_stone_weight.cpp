#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        if (stones.size() == 1) {
            return stones[0];
        }
        sort(stones.begin(), stones.end());
        while (stones.size() > 2) {
            int a = stones.back();
            stones.pop_back();

            int b = stones.back();
            stones.pop_back();

            auto it = std::lower_bound(stones.begin(), stones.end(), abs(a-b));
            stones.insert(it, abs(a-b));
        }
        return abs(stones[0] - stones[1]);
    }
};