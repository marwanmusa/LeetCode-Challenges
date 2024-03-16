class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(math.sqrt(area)), -1, -1):
            w = i
            l = area // i
            if w * l == area:
                return [l, w]

    # Shorter version
    def constructRectangle(self, area: int) -> list[int]:
        for l in range(int(area**0.5), 0, -1):
            if area % l == 0:
                return [area // l, l]