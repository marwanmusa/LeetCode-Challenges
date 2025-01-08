#include <vector>
using namespace std;

class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int res = 0;
        for (vector<int>& row: grid) {
            res += count(row);
        }
        return res;
    }

    int count(vector<int>& row) {
        int i = 0, j = row.size() - 1, neg = 0;
        if (j == i) return row[i] < 0? 1 : 0;
        while (i < j) {
            if (row[i] >= 0 && row[j] >= 0) break;
            else if (row[i] < 0 && row[j] < 0) {
                neg += (j - i + 1);
                break;
            }
            else if (row[i] < 0 && row[j] >= 0) {
                neg += 1;
                i += 1;
            }
            else {
                neg += 1;
                j -= 1;
            }
        }
        return neg;
    }
};