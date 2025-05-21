#include <map>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string reformatDate(string date) {
        vector<string> datev;
        string temp = "", sep = "-", ans = "";
        map<string, string> months
        {
            { "Jan", "01" },
            { "Feb", "02" },
            { "Mar", "03" },
            { "Apr", "04" },
            { "May", "05" },
            { "Jun", "06" },
            { "Jul", "07" },
            { "Aug", "08" },
            { "Sep", "09" },
            { "Oct", "10" },
            { "Nov", "11" },
            { "Dec", "12" }
        };
        for (char w : date) {
            if (w == ' ') {
                datev.push_back(temp);
                temp = "";
            }
            else temp += w;
        }
        ans += temp + sep + months[datev[1]] + sep;
        ans += datev[0].size() == 3? "0" + datev[0].substr(0, 1) : datev[0].substr(0, 2);
        return ans;
    }
};