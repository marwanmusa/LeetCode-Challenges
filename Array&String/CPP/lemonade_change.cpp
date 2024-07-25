#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        map<int, int> change{
            {5, 0},
            {10, 0},
            {20, 0},
        };
        for (int n : bills) {
            change[n] += 1;
            if (n == 5) continue;
            if (n == 10) {
                if (change[5] == 0) return false;
                else change[5] -= 1;
            }
            else {
                if (change[5] == 0) return false;
                else {
                    if (change[10] == 0) {
                        if (change[5] >= 3) {
                            change[5] -= 3;
                            continue;
                            }
                        else return false;
                    }
                    change[10] -= 1;
                    change[5] -= 1;
                }
            }
        }
        
        return true;
    }
};