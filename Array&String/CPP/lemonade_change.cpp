#include <vector>
using namespace std;

class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int change = 0;
        for (int i : bills) {
            if (i == 5) change += i;
            else {
                if ((i - 5) <= change) {
                    change -= (i - 5);
                    change += 5;
                }
                else return false;
            }
        }
        return true;
    }
};