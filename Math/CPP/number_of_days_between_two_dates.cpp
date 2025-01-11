#include <algorithm>
#include <string>
using namespace std;

class Solution {
public:
    int daysBetweenDates(string date1, string date2) {
        if (date1 > date2) swap(date1, date2); // Ensure date1 <= date2

        int date1Y = stoi(date1.substr(0, 4)),
            date1M = stoi(date1.substr(5, 2)),
            date1D = stoi(date1.substr(8, 2));
        int date2Y = stoi(date2.substr(0, 4)),
            date2M = stoi(date2.substr(5, 2)),
            date2D = stoi(date2.substr(8, 2));

        return daysFromStart(date2Y, date2M, date2D) - daysFromStart(date1Y, date1M, date1D);
    }

private:
    int daysFromStart(int year, int month, int day) {
        int days[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int totalDays = 0;

        // Add days for full years
        for (int y = 1971; y < year; ++y) {
            totalDays += 365 + (isLeap(y) ? 1 : 0);
        }

        // Add days for full months of the current year
        for (int m = 1; m < month; ++m) {
            totalDays += days[m];
            if (m == 2 && isLeap(year)) totalDays += 1; // Add leap day
        }

        // Add remaining days of the current month
        totalDays += day;

        return totalDays;
    }

    bool isLeap(int year) {
        return (year % 4 == 0) && (year % 100 != 0 || year % 400 == 0);
    }
};