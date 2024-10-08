#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        unordered_map<string, int> mails;
        for (string mail: emails) {
            string temp = "";
            bool domain = false, add = true;
            for (int i = 0; i < mail.size(); i++) {
                if (mail[i] == '@') {
                    domain = true;
                    temp += mail[i];
                    i++;
                }
                if (domain) {
                    temp += mail[i];
                }
                else {
                    if (mail[i] != '.' && mail[i] != '+' && add) {
                        temp += mail[i];
                    }
                    if (mail[i] == '+') add = false;
                }
            }
            mails[temp] += 1;
        }
        return mails.size();
    }

    //shorter
    int numUniqueEmails(vector<string>& emails) {
        unordered_set<string> mails;
        for (string &mail: emails) {
            string temp;
            for (char &c: mail) {
                if (c == '+' || c == '@') break;
                if (c == '.') continue;
                temp += c;
            }
            temp += mail.substr(mail.find('@'));
            mails.insert(temp);
        }
        return mails.size();
    }
};