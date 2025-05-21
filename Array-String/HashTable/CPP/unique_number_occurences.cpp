#include <algorithm>
#include <set>
#include <unordered_map>
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

    // without map and set
    bool uniqueOccurrences(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        vector<int> v;

        for (int i = 0; i < arr.size(); i++) {
            int cnt = 1;

            // Count occurrences of the current element
            while (i + 1 < arr.size() && arr[i] == arr[i + 1]) {
                cnt++;
                i++;
            }

            v.push_back(cnt);
        }

        sort(v.begin(), v.end());

        for (int i = 1; i < v.size(); i++) {
            if (v[i] == v[i - 1]) {
                return false;
            }
        }

        return true;
    }
};