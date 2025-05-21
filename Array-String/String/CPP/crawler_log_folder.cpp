#include <vector>
#include <string>
#include <algorithm> // for std::max
using namespace std;
// 1598. Crawler Log Folder
// https://leetcode.com/problems/crawler-log-folder/description/

class Solution {
    public:
        int minOperations(vector<string>& logs) {
            int distance = 0;

            for (string log : logs) {
                if (log == "../") {
                    distance = max(0, distance - 1);
                } else if (log != "./") {
                    distance++;
                }
            }

            return distance;
        }
    };