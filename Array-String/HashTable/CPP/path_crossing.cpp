#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    bool isPathCrossing(string path) {
        int n = path.size();
        if (n == 1) return false;
        unordered_map<char, vector<int>> direction;
        direction['N'] = {0, 1};
        direction['S'] = {0, -1};
        direction['E'] = {1, 0};
        direction['W'] = {-1, 0};
        int x = 0, y = 0;
        unordered_map<int, unordered_map<int, bool>> visited;
        visited[x][y] = true;
        for (int i = 0; i < n; i++) {
            x += direction[path[i]][0];
            y += direction[path[i]][1];
            if (visited[x][y]) return true;
            visited[x][y] = true;
        }
        return false;
    }
};