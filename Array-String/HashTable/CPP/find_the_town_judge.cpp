#include <vector>
using namespace std;

class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<int> town_judge(n+1, 0);
        for (vector<int> rel: trust) {
            town_judge[rel[0]]--;
            town_judge[rel[1]]++;
        }

        for (int i = 1; i < n+1; i++) {
            if (town_judge[i] == n-1) return i;
        }
        return -1;
    }
};