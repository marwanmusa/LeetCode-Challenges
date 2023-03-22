import math
import collections
from typing import List

class Solution:
    """
    Task:
    You are given a positive integer n representing n cities numbered from 1 to n.
    You are also given a 2D array roads where roads[i] = [ai, bi, distance-i] indicates that
    there is a bidirectional road between cities ai and bi with a distance equal to distance-i.
    The cities graph is not necessarily connected.

    The score of a path between two cities is defined as the minimum distance of a road in this path.

    Return the minimum possible score of a path between cities 1 and n.

    Note:
    - A path is a sequence of roads between two cities.
    - It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
    - The test cases are generated such that there is at least one path between 1 and n.
        """
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        ans = math.inf
        q = collections.deque([1])
        seen = {1}

        # bidirectional path
        for u, v, distance in roads:
            graph[u].append((v, distance))
            graph[v].append((u, distance))

        # starts from city-1
        while q:
            u = q.popleft()
            for v, d in graph[u]:
                ans = min(ans, d)
                if v in seen:
                    continue
                q.append(v)
        return ans