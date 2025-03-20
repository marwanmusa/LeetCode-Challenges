from typing import List
from collections import Counter

class Solution:
    """
    Task:
    You are given an integer n. There is an undirected graph with n nodes,
    numbered from 0 to n - 1. You are given a 2D integer array edges where
    edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

    Return the number of pairs of different nodes that are unreachable from each other.
    """
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            if parent_x == parent_y:
                return
            uf[parent_x] = parent_y

        uf = list(range(n))
        for a, b in edges:
            union(a, b)

        counts = Counter([find(i) for i in range(n)])

        res = 0
        for k in counts:
            n -= counts[k]
            res += n * counts[k]
        return res