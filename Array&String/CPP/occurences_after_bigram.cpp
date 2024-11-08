#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> findOcurrences(string textt, string first, string second) {
        vector<string> text = split(textt, ' '), res;

        for (int i = 0; i < text.size()-2; i++) {
            if (text[i] == first && text[i+1] == second) res.push_back(text[i+2]);
        }
        return res;
    }
    vector<string> split (const string &s, char delim) {
        vector<std::string> result;
        stringstream ss (s);
        string item;

        while (getline (ss, item, delim)) {
            result.push_back (item);
        }

        return result;
    }

};