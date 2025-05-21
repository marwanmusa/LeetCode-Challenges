#include <algorithm>
#include <vector>
#include <string>
using namespace std;

class Solution {
    public:
        vector<string> removeAnagrams(vector<string>& words) {
            int n = words.size();
            vector<string> res;
            string prev;

            for (string s: words) {
                string cur = s;
                sort(cur.begin(), cur.end());
                if (prev != cur) {
                    res.push_back(s);
                    prev = cur;
                }
            }
            return res;
        }
    };