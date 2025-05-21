#include <vector>
using namespace std;

class Solution {
public:
    int numRookCaptures(vector<vector<char>>& board) {
        vector<int> pos = search(board);
        int x0 = pos[0], y0 = pos[1], ans = 0;
        vector<vector<int>> moves = {{1,0}, {0,1}, {-1,0}, {0, -1}};
        for (auto move : moves) {
            int x = x0 + move[0];
            int y = y0 + move[1];
            while (x >= 0 && x < 8 && y >= 0 && y < 8) {
                if (board[x][y] == 'p') ans++;
                if (board[x][y] != '.') {
                    break;
                }
                x += move[0];
                y += move[1];
            }
        }
        return ans;
    }

    vector<int> search(vector<vector<char>>& board) {
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                if (board[i][j] == 'R') return vector<int>{i, j};
            }
        }
        return vector<int>{};
    }
};