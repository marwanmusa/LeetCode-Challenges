#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_map<string, string> d;
        string dest = paths[0][0];
        for (vector<string> p : paths) d[p[0]] = p[1];
        while (d.count(dest) == 1) dest = d[dest];
        return dest;
    }
};