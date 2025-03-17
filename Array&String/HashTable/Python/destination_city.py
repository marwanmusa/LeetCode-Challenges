from collections import defaultdict

class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        d = defaultdict(str)
        dest = paths[0][0]
        for p in paths:
            d[p[0]] = p[1]
        while d.get(dest):
            dest = d.get(dest)
        return dest