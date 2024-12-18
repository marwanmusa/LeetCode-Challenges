class Solution {
public:
    int subtractProductAndSum(int n) {
        int mult = 1, adds = 0;
        while (n > 0) {
            int cur = n % 10;
            mult *= cur;
            adds += cur;
            n /= 10;
        }
        return mult - adds;
    }
};