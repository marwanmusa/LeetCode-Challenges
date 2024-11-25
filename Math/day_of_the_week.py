class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        if month < 3:
            month += 12
            year -= 1
        k, j = year % 100, year // 100
        h = (((day + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7) + 7) % 7
        return days[h]