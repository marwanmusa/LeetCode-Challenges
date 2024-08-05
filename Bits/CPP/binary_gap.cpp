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


    // approach 2
    // This approach is a bit more efficient because it uses a single pass over the binary representation
    int binaryGap2(int N) {
        int res = 0;
        for (int d = -32; N; N /= 2, d++)
            if (N % 2) res = max(res, d), d = 0;
        return res;
    }
    
};