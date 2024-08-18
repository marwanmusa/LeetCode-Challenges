#include <numeric>
#include <map>
#include <vector>
using namespace std;

class Solution {
public:
    bool hasGroupsSizeX(vector<int>& deck) {
        map<int, int> counter;
        int res;
        for (int n: deck) counter[n] += 1;
        for (auto i : counter) res = __gcd(i.second, res);
        return res > 1;
    }
};