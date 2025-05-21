#include <string>

#include <vector>

using namespace std;

// Solution 1: Using two pointers to keep track of unique characters and remove duplicate

class Solution {
public:
    string removeDuplicates(string s) {
        vector<char> stk;
        for (char a: s) {
            if (stk.size() == 0) {
                stk.push_back(a);
            }
            else {
                if (stk.back() == a) stk.pop_back();
                else stk.push_back(a);
            }
        }
        return string(stk.begin(), stk.end());
    }
};