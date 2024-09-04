#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> diStringMatch(string s) {
        int i = 0, j = s.size();
        vector<int> ans;
        for (char c : s) {
            if (c == 'D') {
                ans.push_back(j);
                j--;
            } else {
                ans.push_back(i);
                i++;
            }
        }
        ans.push_back(i);
        return ans;
    }
};