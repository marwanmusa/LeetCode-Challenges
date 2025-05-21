#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
// 150. Reorder Spaces Between Words
// https://leetcode.com/problems/reorder-spaces-between-words/description/


class Solution {
    public:
        string reorderSpaces(string text) {
            int spaces = count(text.begin(), text.end(), ' ');
            vector<string> words;
            istringstream iss(text);
            string token;

            while (getline(iss, token, ' ')) {
                if (!token.empty()) words.push_back(token);
            }

            int n = words.size();

            if (n == 1) return words[0] + string(spaces, ' ');

            int partition = spaces / (n - 1), extra = spaces % (n - 1);

            string spaceparts(partition, ' '), spaceextra(extra, ' ');

            ostringstream oss;
            for (int i = 0; i < n; ++i) {
                if (i > 0) oss << spaceparts;
                oss << move(words[i]);
            }
            return oss.str() + spaceextra;

        }
    };