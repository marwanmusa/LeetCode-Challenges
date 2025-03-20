class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        if len(coordinates) == 2: return True
        xs, ys = coordinates[1][0] - coordinates[0][0], coordinates[1][1] - coordinates[0][1]
        for i in range(2, len(coordinates)):
            curxs, curys = coordinates[i][0] - coordinates[i-1][0], coordinates[i][1] - coordinates[i-1][1]
            if xs * curys != ys * curxs: return False
        return True

    # simpler
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        if len(coordinates) == 2: return True
        (x0, y0), (x1, y1) = coordinates[:2]
        for x, y in coordinates[2:]:
            if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0): return False
        return True
