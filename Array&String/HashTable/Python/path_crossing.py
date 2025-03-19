# Problem: Path Crossing
# Difficulty: Easy
from collections import defaultdict

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        n = len(path)
        if n == 1: return False
        d = {"N" : (0, 1), "S" : (0, -1), "E" : (1, 0), "W" : (-1, 0)}
        cur = (0, 0)
        mem = {cur}
        for c in path:
            cur = (cur[0]+d[c][0], cur[1]+d[c][1])
            if cur in mem: return True
            mem.add(cur)
        return False

    # variation 2
    def isPathCrossing(self, path: str) -> bool:
        n = len(path)
        if n == 1: return False
        direction = {"N" : (0, 1), "S" : (0, -1), "E" : (1, 0), "W" : (-1, 0)}
        x, y = 0, 0
        visited = dict()
        visited[(x, y)] = True
        for c in path:
            x += direction[c][0]
            y += direction[c][1]
            if visited.get((x, y)): return True
            visited[(x, y)] = True
        return False

    # variation 3
    def isPathCrossing(self, path: str) -> bool:
        n = len(path)
        if n == 1: return False
        direction = {"N" : (0, 1), "S" : (0, -1), "E" : (1, 0), "W" : (-1, 0)}
        x, y = 0, 0
        visited = defaultdict(lambda : defaultdict(bool))
        visited[x] = {y: True}
        for c in path:
            x += direction[c][0]
            y += direction[c][1]
            if visited.get(x) and visited[x].get(y): return True
            visited[x][y] = True
        return False