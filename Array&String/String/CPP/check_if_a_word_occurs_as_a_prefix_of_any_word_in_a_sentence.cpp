#include <string>
using namespace std;

class Solution {
public:
    int isPrefixOfWord(string sentence, string searchWord) {
        int idx = 0;
        string temp = "";
        char del = ' ';
        for (char x: sentence) {
            if (x != del) temp += x;
            else {
                if (temp.size() != 0) {
                    idx++;
                    if (temp.find(searchWord) == 0) return idx;
                    temp = "";
                }
            }
        }
        return temp.find(searchWord) == 0 ? idx + 1 : -1;
    }
};