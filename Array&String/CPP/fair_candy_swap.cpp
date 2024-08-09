#include <numeric>
#include <vector>
#include <set>
using namespace std;

class Solution {
public:
    vector<int> fairCandySwap(vector<int>& aliceSizes, vector<int>& bobSizes) {
        int suma = accumulate(aliceSizes.begin(), aliceSizes.end(), 0);
        int sumb = accumulate(bobSizes.begin(), bobSizes.end(), 0);
        int diff = suma - sumb;
        
        set<int> aliceSet(aliceSizes.begin(), aliceSizes.end());
        
        for (int b : bobSizes) {
            int a = b + diff / 2;
            if (aliceSet.find(a)!= aliceSet.end()) {
                return {a, b};
            }
        }
        return vector<int>{};
    }
};