#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string tictactoe(vector<vector<int>>& moves) {
        vector<vector<int>> moveA, moveB;
        for (int i = 0; i < moves.size(); i++) {
            if (i % 2 == 0) moveA.push_back(moves[i]);
            else moveB.push_back(moves[i]);
        }
        return isWin(moveA)? "A" : isWin(moveB)? "B" : moves.size() == 9? "Pending" : "Draw";
    }

    bool isWin(vector<vector<int>>& moves) {
        for (int i = 0; i < 3; i++) {
            int lsum = 0, rsum = 0;
            for (vector<int> vec : moves) {
                lsum += vec[0] == i ? 1 : 0;
                rsum += vec[1] == i ? 1 : 0;
            }
            if (lsum >= 3 || rsum >= 3) return true;
        }
        vector<int> lu(2, 0),
                    rd(2, 2),
                    mi(2, 1),
                    ru = {0, 2},
                    ld = {2, 0};
        if (((find(moves.begin(), moves.end(), lu) != moves.end()) &&
             (find(moves.begin(), moves.end(), rd) != moves.end()) &&
             (find(moves.begin(), moves.end(), mi) != moves.end())) ||
            ((find(moves.begin(), moves.end(), ru) != moves.end()) &&
             (find(moves.begin(), moves.end(), ld) != moves.end()) &&
             (find(moves.begin(), moves.end(), mi) != moves.end()))) return true;
        return false;
    }
};