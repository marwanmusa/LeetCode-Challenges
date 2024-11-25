#include <string>
using namespace std;

class Solution {
public:
    // using zeller's congruence
    string dayOfTheWeek(int day, int month, int year) {
        string days[7] = {"Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"};
        if (month <= 2) {
            month += 12;
            year--;
        }
        int k = year % 100, j = year / 100;
        int h = (day + ((13 * (month + 1)) / 5) + k + (k / 4) + (j / 4) - (2 * j)) % 7;
        h = (h + 7) % 7;
        return days[h];
    }
};