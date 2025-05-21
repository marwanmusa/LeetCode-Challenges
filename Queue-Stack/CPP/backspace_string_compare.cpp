class Solution {
public:
    bool backspaceCompare(string s, string t) {
        return st(s) == st(t);
    }

    string st(string s) {
        string curs;
        for (char e : s) {
            if (e != '#') curs.push_back(e); 
            else if (!curs.empty()) curs.pop_back();
        }
        return curs;
    }
};