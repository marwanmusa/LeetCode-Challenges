class Solution:
    def containsPattern(self, arr: list[int], m: int, k: int) -> bool:
        n = len(arr)
        for i in range(n + 1 - m * k):
            match = True
            for j in range(0, m * (k - 1)):
                if arr[i+j] != arr[i+j+m]:
                    match = False
                    break
            if match: return True
        return False