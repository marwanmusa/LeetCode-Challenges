class Solution:
    def dayOfYear(self, date: str) -> int:
        days_freq = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        y, m, d = map(int, date.split('-'))

        if self.is_leap_year(y):
            days_freq[2] = days_freq[2] + 1

        ndays = 0
        for i in range(m):
                ndays += days_freq[i]

        return ndays + min(days_freq[m], d)

    def is_leap_year(self, y: int) -> bool:
        return (y % 4 == 0 and y % 100 != 0) or (y % 4 == 0 and y % 100 == 0 and y % 400 == 0)