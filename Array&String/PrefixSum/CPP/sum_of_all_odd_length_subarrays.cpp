#include <iostream>
#include <vector>
using namespace std;
// 1588. Sum of All Odd Length Subarrays
// https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        int n = arr.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            int left = i + 1, right = n - i;
            int total = left * right;
            int odd = total / 2;
            ans += arr[i] * (odd + (total % 2));
        }
        return ans;
    }
};