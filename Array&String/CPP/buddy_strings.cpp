class Solution {
public:
    bool buddyStrings(string s, string goal) {
        if (s.size() != goal.size()) return false;
        set<char> ss;
        for (char  e: s) ss.insert(e);
        if (s == goal) return (ss.size() < s.size());
        auto I = -1, J = -1; 
        for (int i = 0; i < s.size(); i++) {
            if (s[i] != goal[i]) {
                if (I == -1) I = i;
                else if (J == -1) J = i;
                else return false;
            }
        }
        if (J == -1) return false;
        return s[I] == goal[J] && s[J] == goal[I]; 
    }
};