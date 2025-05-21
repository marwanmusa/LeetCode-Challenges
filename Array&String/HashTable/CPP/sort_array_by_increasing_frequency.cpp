#include <vector>
#include <unordered_map>
#include <algorithm>
#include <functional>
using namespace std;
// 1636. Sort Array by Increasing Frequency
// https://leetcode.com/problems/sort-array-by-increasing-frequency/description/
// Given an array of integers nums, sort the array in increasing order based on the frequency of the values.

class Solution {
    public:
        vector<int> frequencySort(vector<int>& nums) {
            unordered_map<int, int> freqs;
            for (const int x : nums) freqs[x]++;

            unordered_map<int, vector<int>> freqToNums;
            for (const auto& [n, freq] : freqs) {
                freqToNums[freq].push_back(n);
            }

            vector<int> res;
            for (auto& [f, numsAtFreq] : freqToNums) {
                sort(numsAtFreq.begin(), numsAtFreq.end(), greater<>());
                for (const int num : numsAtFreq) {
                    res.insert(res.end(), f, num);
                }
            }

            return res;
        }
    };

    // using sort with custom comparator
    class Solution2 {
        public:
            vector<int> frequencySort(vector<int>& nums) {
                unordered_map<int, int> freqs;
                for (const int x : nums) freqs[x]++;

                sort(nums.begin(), nums.end(), [&](int a, int b) {
                    return freqs[a] == freqs[b] ? a > b : freqs[a] < freqs[b];
                });

                return nums;
            }
        };
