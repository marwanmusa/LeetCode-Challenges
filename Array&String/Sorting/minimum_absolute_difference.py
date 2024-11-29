class Solution:
    def minimumAbsDifference(self, arr:list[int]) -> list[list[int]]:
        arr = sorted(arr)
        threshold = float('inf')
        res = []
        for i in range(len(arr) - 1):
            a, b = arr[i], arr[i+1]
            diff = b - a
            if diff < threshold:
                threshold = diff
                res = []
            elif diff > threshold: continue
            res.append([a, b])
        return res