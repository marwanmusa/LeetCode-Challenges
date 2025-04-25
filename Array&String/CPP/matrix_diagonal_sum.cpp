#include <vector>
using namespace std;

class Solution {
    public:
        int diagonalSum(vector<vector<int>>& mat) {
            int n = mat.size(), ans = 0;
            int odd = n & 1, mid = n / 2;
            for (int i = 0; i < n; i++) {
                if (odd && i == mid) ans += mat[i][i];
                else ans += mat[i][i] + mat[i][n-i-1];
            }
            return ans;
        }
    };