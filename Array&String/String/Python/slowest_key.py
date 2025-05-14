class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        longest, maxkey, n = releaseTimes[0], keysPressed[0], len(releaseTimes)
        durations = [0] * n
        durations[0] = releaseTimes[0]
        for i in range(1, n):
            durations[i] = releaseTimes[i] - releaseTimes[i-1]
            if longest < durations[i] or (longest == durations[i] and maxkey < keysPressed[i]):
                longest = durations[i]
                maxkey = keysPressed[i]
        return maxkey