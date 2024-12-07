#include <string>
using namespace std;

class Solution {
public:
    int balancedStringSplit(string s) {
        int l = 0, r = 0, res = 0;
        for (char w : s) {
            if (w == 'L') l++;
            else r++;

            if (l == r) {
                res++;
                l = 0;
                r = 0;
            }
        }
        return res;
    }
};