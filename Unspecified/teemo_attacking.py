class Solution:
    """
    Task:
    Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe,
    Ashe gets poisoned for a exactly duration seconds. More formally,
    an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1].
    If Teemo attacks again before the poison effect ends, the timer for it is reset,
    and the poison effect will end duration seconds after the new attack.

    You are given a non-decreasing integer array timeSeries,
    where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i],
    and an integer duration.

    Return the total number of seconds that Ashe is poisoned.
    """
    # Time limit exceed
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        collect = [range(x, x+duration) for x in timeSeries]
        return len(set(x for j in collect for x in j))

    # brute-force approach
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        ans = duration * len(timeSeries)
        for i in range(1, len(timeSeries)):
            ans -= max(0, duration - (timeSeries[i] - timeSeries[i-1]))
        return ans