#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int n = strs[0].size();
        vector<int> idxs(n);
        string cur = strs[0];
        iota(idxs.begin(), idxs.end(), 0);
        for (int i = 1; i < strs.size(); i++) {
            vector<int> stack = idxs;
            for (int idx : idxs) {
                if (strs[i][idx] < cur[idx]) {
                    auto it = find(stack.begin(), stack.end(), idx);
                    stack.erase(it);
                }
            }
            idxs = stack;
            cur = strs[i];
        }
        return n - idxs.size();
    }
};