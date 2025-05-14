#include <iostream>
#include <vector>
#include <string>
using namespace std;
// LeetCode 1629. Slowest Key
// https://leetcode.com/problems/slowest-key/description/

class Solution {
    public:
        char slowestKey(vector<int>& releaseTimes, string keysPressed) {
            int longest = releaseTimes[0], n = releaseTimes.size();
            char maxkey = keysPressed[0];
            vector<int> durations(n, 0);
            durations[0] = releaseTimes[0];
            for (int i = 1; i < n; i++) {
                durations[i] = releaseTimes[i] - releaseTimes[i-1];
                if (longest < durations[i] || (longest == durations[i] && maxkey < keysPressed[i])) {
                    longest = durations[i];
                    maxkey = keysPressed[i];
                }
            }
            return maxkey;
        }
    };