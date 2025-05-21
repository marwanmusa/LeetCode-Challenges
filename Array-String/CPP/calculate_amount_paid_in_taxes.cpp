#include <algorithm>
#include <vector>
using namespace std;

class Solution {
    public:
        double calculateTax(vector<vector<int>>& brackets, int income) {
            double ans = 0;
            int prev = 0;
            for (const auto& bracket : brackets) {
                ans += min(bracket[0] - prev, income) * (bracket[1] / 100.0);
                income -= (bracket[0] - prev);
                prev = bracket[0];
                if (income < 0) break;
            }
            return ans;
        }
    };