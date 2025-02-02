class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        ans = 0
        for a, b in zip(startTime, endTime):
            if a <= queryTime <= b: ans += 1
        return ans

    # shorter
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        return sum(s <= queryTime <= e for s, e in zip(startTime, endTime))