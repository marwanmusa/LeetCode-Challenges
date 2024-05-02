#include <algorithm> 
#include<iostream>
#include<string>
using namespace std; 

class Solution {
public:
    string reverseStr(string s, int k) {
        int i = 0, n = s.size();
        while (i < s.size()) {
            if (i + k < n) {
                reverse(s.begin()+i, s.begin()+i+k);
                i += 2*k;
            }
            else {
                reverse(s.begin()+i, s.end());
                break;
            }
        }
        return s;
    }
};