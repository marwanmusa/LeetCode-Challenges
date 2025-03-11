class Solution:
    def trimMean(self, arr: list[int]) -> float:
        n, cut = len(arr), len(arr) // 20
        return sum(sorted(arr)[cut:-cut]) / (n - (2 * cut))