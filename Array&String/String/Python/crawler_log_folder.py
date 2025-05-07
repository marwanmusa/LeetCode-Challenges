class Solution:
    def minOperations(self, logs: list[str]) -> int:
        distance = 0
        for log in logs:
            if log == "../": distance = max(0, distance - 1)
            elif log != "./": distance += 1
        return distance
