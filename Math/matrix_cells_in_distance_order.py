from collections import defaultdict
from itertools import product

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:
        dist = lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter)
        hmap = defaultdict(list)
        mat = product(range(rows), range(cols))
        for coor in mat:
            hmap[dist(coor)].append(coor)
        res = []
        for i in range(max(hmap) + 1):
            res.extend(hmap[i])
        return res
