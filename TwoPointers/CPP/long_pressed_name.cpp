#include <string>
using namespace std;

class Solution {
public:
    bool isLongPressedName(string name, string typed) {
        int i = 0,
            j = 0,
            cntn = 0,
            cntt = 0,
            m = name.size(),
            n = typed.size();
        char cur = name[0];
        if (name[0] != typed[0]) return false;
        while (i < m) {
            char cur = name[i];
            if (cur != typed[j]) return false;
            while (j < n && typed[j] == cur) {
                cntt++;
                j++;
            }
            while (i < m && name[i] == cur) {
                cntn++;
                i++;
            }
            if (cntt < cntn || (j < n && i >= m) || j >= n && i < m) return false;
            cntn = 0;
            cntt = 0;
        }
        return true;
    }
};