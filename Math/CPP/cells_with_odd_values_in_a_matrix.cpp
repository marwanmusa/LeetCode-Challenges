#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int oddCells(int m, int n, vector<vector<int>>& indices) {
        vector<int> rows(m, 0);
        vector<int> cols(n, 0);

        for (const auto& idx : indices) {
            rows[idx[0]] ^= 1;
            cols[idx[1]] ^= 1;
        }

        int oddR = count(rows.begin(), rows.end(), 1);
        int oddC = count(cols.begin(), cols.end(), 1);
        int evenR = m - oddR;
        int evenC = n - oddC;
        return oddR * evenC + evenR * oddC;
    }
};