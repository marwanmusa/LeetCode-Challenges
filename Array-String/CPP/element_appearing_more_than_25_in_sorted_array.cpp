#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        int limit = arr.size() / 4;
        unordered_map<int, int> mp;
        for (int n: arr) {
            mp[n]++;
            if (mp[n] > limit) return n;
        }
        return -1;
    }

    // memory efficient implementation
    int findSpecialInteger(vector<int>& arr) {
        int limit = arr.size() / 4;
        int count = 1, special = arr[0];
        for (int i = 1; i < arr.size(); i++) {
            if (arr[i] == special) count++;
            else count = 1;
            if (count > limit) return special;
            special = arr[i];
        }
        return special;
    }
};