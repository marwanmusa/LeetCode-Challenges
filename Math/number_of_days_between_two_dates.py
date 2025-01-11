class Solution:
    def isLeap(self, year) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    def daysFromStart(self, year, month, day) -> int:
        days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        totalDays = 0
        for y in range(1971, year): totalDays += 366 if self.isLeap(y) else 365
        for m in range(1, month): totalDays += days[m] + 1 if self.isLeap(year) and m == 2 else days[m]
        totalDays += day
        return totalDays
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if date1 > date2: date1, date2 = date2, date1
        y1, m1, d1 = map(int, date1.split("-"))
        y2, m2, d2 = map(int, date2.split("-"))
        return self.daysFromStart(y2, m2, d2) - self.daysFromStart(y1, m1, d1)
