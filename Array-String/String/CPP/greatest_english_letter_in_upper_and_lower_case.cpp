#include <string>
using namespace std;

class Solution {
    public:
        string greatestLetter(string s) {
            for (int i = 25; i > -1; i--) {
                char up = 65 + i,
                     low = 97 + i;
                if (s.find(up) != string::npos && s.find(low) != string::npos) return string(1, up);
            }
            return "";
        }
    };