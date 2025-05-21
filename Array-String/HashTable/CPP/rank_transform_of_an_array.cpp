#include <algorithm>
#include <map>
#include <set>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        vector<int> temp = arr;
        sort(temp.begin(), temp.end());
        int cnt = 1;
        map<int, int> rank;
        for (int x: temp) {
            if (rank.count(x) == 1) continue;
            rank[x] = cnt;
            cnt++;
        }

        vector<int> ans;
        for (int x: arr) ans.push_back(rank[x]);
        return ans;
    }

    // without mapping
    vector<int> arrayRankTransform(vector<int>& arr) {
        set<int> rank(arr.begin(), arr.end());
        vector<int> temp(rank.begin(), rank.end());

        vector<int> ans;
        for (int x: arr) {
            auto it = find(temp.begin(), temp.end(), x);
            ans.push_back(it - temp.begin() + 1);
        }
        return ans;
    }
};