#include <string>
using namespace std;

class Solution {
public:
    int binaryGap(int n) {
        char one = '1';
        int ones = 0, cur = -1, d = 0;
        string bin_rep = toBinary(n);
        for (int i = 0; i < bin_rep.size(); i++) {
            if (bin_rep[i] == one) {ones += 1;}
        }
        if (ones < 2) return 0;
        else {
            for (int i = 0; i < bin_rep.size(); i++) {
                if (bin_rep[i] == one) {
                    if (cur!= -1) d = max(d, i - cur);
                    cur = i;
                }
            }
            return d;
        }
    }

    string toBinary(int n) {
        string r;
        while(n!=0) {r=(n%2==0 ?"0":"1")+r; n/=2;}
        return r;
    }
};