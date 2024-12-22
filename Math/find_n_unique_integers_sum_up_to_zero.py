class Solution:
    def sumZero(self, n: int) -> list[int]:
        start = n // 2
        if not n & 1:
            return [x for x in range(-start, start+1) if x != 0]
        else:
            return [x for x in range(-start, start+1)]