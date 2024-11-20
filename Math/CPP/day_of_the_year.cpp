#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int dayOfYear(string date) {
        // Days in each month
        int days_freq[13] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        int year = stoi(date.substr(0, 4)),
            month = stoi(date.substr(5, 2)),
            day = stoi(date.substr(8, 2));
        if (isLeapYear(year)) days_freq[2]++;
        int sum = 0;
        for (int i = 0; i < month - 1; i++) sum += days_freq[i];
        return sum + min(sum, days_freq[month]);
    }

    bool isLeapYear(const int year) {
        return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0 && year % 4 == 0 && year % 100 == 0);
    }
};