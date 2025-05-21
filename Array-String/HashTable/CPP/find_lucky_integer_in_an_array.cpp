#include <map>
#include <vector>
using namespace std;

class Solution {
public:
    int findLucky(vector<int>& arr) {
        int luckynum = -1;
        map<int, int> cnt;
        for (int x: arr) cnt[x]++;
        for (auto const [k, v] : cnt) if (k == v) luckynum = max(luckynum, k);
        return luckynum;
    }
};