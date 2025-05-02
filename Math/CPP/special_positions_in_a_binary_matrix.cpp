#include <vector>
using namespace std;
// 1572. Matrix Diagonal Sum
// https://leetcode.com/problems/special-positions-in-a-binary-matrix/
// Given a binary matrix mat, return the number of special positions in it.
// A position (i,j) of a matrix is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).


class Solution {
    public:
        int numSpecial(vector<vector<int>>& mat) {
            int r = mat.size(), c = mat[0].size();
            vector<int> rSum(r, 0), cSum(c, 0);

            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    if (mat[i][j] == 1) {
                        rSum[i]++;
                        cSum[j]++;
                    }
                }
            }
            int ans = 0;
            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    if (mat[i][j] == 1 && rSum[i] == 1 && cSum[j] == 1) {
                        ans++;
                    }
                }
            }
            return ans;
        }
    };