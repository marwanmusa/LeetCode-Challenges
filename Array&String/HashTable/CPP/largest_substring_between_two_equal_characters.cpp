#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
using namespace std;
// 1624. Largest Substring Between Two Equal Characters
// https://leetcode.com/problems/largest-substring-between-two-equal-characters/
// Given a string s, return the length of the longest substring between two equal characters, excluding the two characters.
// If there is no such substring return -1.

class Solution {
    public:
        unordered_map<char, int> counter(const string& input) {
            unordered_map<char, int> freq;
            for (char c : input) {
                freq[c]++;
            }
            return freq;
        }

        int maxLengthBetweenEqualCharacters(string s) {
            auto counts = counter(s);
            vector<char> limiters;
            int maxLength = -1;
            for (const auto& [ch, cnt] : counts) {
                if (cnt >= 2) limiters.push_back(ch);
            }
            for (char limiter : limiters) {
                int l = 0, r = s.size() - 1;
                while (r - l - 1 > maxLength) {
                    if (s[l] == limiter && s[r] == limiter) maxLength = max(r-l-1, maxLength);
                    if (s[l] != limiter) l++;
                    if (s[r] != limiter) r--;
                }
            }
            return maxLength;
        }
    };