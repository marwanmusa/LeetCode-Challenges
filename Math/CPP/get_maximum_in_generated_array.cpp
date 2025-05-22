#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
// Problem: 1646. Get Maximum in Generated Array
// URL: https://leetcode.com/problems/get-maximum-in-generated-array/
// Difficulty: Easy

class Solution {
public:
    int getMaximumGenerated(int n) {
        if (n == 0) return 0;
        vector<int> dp(n + 1, 0);
        dp[0] = 0;
        dp[1] = 1;
        for (int i = 0; i < n + 1; i++) {
            if (i % 2 == 0) dp[i] = dp[i / 2];
            else dp[i] = dp[i / 2] + dp[(i / 2) + 1];
        }
        return *max_element(dp.begin(), dp.end());
    }
};