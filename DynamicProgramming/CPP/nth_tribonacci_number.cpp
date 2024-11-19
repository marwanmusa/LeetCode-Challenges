#include <vector>
using namespace std;

class Solution {
public:
    int tribonacci(int n) {
        vector<int> fn(38, 0);
        fn[0] = 0;
        fn[1] = 1;
        fn[2] = 1;
        if (n < 3) return fn[n];
        for (int i = 3; i < 38; i++) {
            fn[i] = fn[i-1] + fn[i-2] + fn[i-3];
            if (i == n) return fn[n];
        }
        return fn[n];
    }
};