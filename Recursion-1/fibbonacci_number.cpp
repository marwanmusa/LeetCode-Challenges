class Solution {
public:
    int fib(int n) {
        if (n < 2) return n;

        int ans, zero = 0, first = 1;
        for (int i = 2; i <= n; i++) {
            ans = zero + first;
            zero = first;
            first = ans;
        }

        return ans;
    }
};