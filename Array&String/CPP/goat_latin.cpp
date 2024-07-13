#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

class Solution {
public:
    string toGoatLatin(string sentence) {
        sentence += ' ';
        vector<string> arr;
        string temp = "", ma = "ma";
        for (char s : sentence) {
            if (s == ' ') {
                arr.push_back(temp);
                temp = "";
                continue;
            }
            temp += s;   
        }

        set<char> vowels = {'a','i','u','e','o','A','U','E','I','O'};
        string ans;
        for (int i = 0; i < arr.size(); i++) {
            if (vowels.find(arr[i][0]) == vowels.end()) {
                ans += arr[i].substr(1) + arr[i][0] + ma + string((i+1), 'a') + " ";
                continue;
            }
            ans += arr[i] + ma + string((i+1), 'a') + " ";
        }
        if (!ans.empty()) ans.pop_back();
        return ans;
    }
};

int main() {
  Solution sol;

  // Test case 1: Input string with consonant starting word
  string input1 = "I speak Goat Latin";
  string expected1 = "Imaa peaksmaaa oatGmaaaa atinLmaaaaa";
  string result1 = sol.toGoatLatin(input1);
  cout << "Test Case 1: Input - " << input1 << endl;
  cout << "Expected Output - " << expected1 << endl;
  cout << "Result - " << result1 << endl;
  cout << (result1 == expected1 ? "Passed!" : "Failed!") << endl << endl;

  // Test case 2: Input string with vowel starting word
  string input2 = "The world is a stage";
  string expected2 = "heTmaa orldwmaaa ismaaaa amaaaaa tagesmaaaaaa";
  string result2 = sol.toGoatLatin(input2);
  cout << "Test Case 2: Input - " << input2 << endl;
  cout << "Expected Output - " << expected2 << endl;
  cout << "Result - " << result2 << endl;
  cout << (result2 == expected2 ? "Passed!" : "Failed!") << endl;

  // Add more test cases as needed to cover different scenarios

  return 0;
}