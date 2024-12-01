#include <set>
#include <unordered_map>>
#include <vector>
using namespace std;

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> mp;
        for (int n: arr) mp[n]++;
        set<int> occrns;
        for (auto [k, v]: mp) occrns.insert(v);
        return occrns.size() == mp.size();
    }
};