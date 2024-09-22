#include <vector>
using namespace std;

class Solution {
public:
    vector<int> addToArrayForm(vector<int>& num, int k) {
        int i = num.size() - 1;
        while (k > 0) {
            if (i >= 0) {
                k += num[i];
                num[i] = k % 10;
                i -= 1;
            } else {
                num.insert(num.begin(), k % 10);
            }
            k /= 10;
        }
        return num;
    }
};