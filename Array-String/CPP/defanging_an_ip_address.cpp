#include <string>
using namespace std;

class Solution {
public:
    string defangIPaddr(string address) {
        string defanged;
        for (char s : address) {
            if (s == '.') defanged += "[.]";
            else defanged += s;
        }
        return defanged;
    }
};