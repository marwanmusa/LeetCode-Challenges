class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(math.sqrt(area)), -1, -1):
            w = i
            l = area // i
            if w * l == area:
                return [l, w]
