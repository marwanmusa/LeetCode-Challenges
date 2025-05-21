class Solution:
    def addOne(self, visited: dict, l: int, r: int) -> None:
        for k in visited:
            if l <= k <= r:
                visited[k] += 1

    def mostVisited(self, n: int, rounds: list[int]) -> list[int]:
        rounds_len = len(rounds)
        ans, visited, prev = [], {x: 0 for x in range(1, n+1)}, rounds[0]
        visited[rounds[0]] += 1
        for i in range(1, rounds_len):
            prev = rounds[i - 1]
            cur = rounds[i]
            if cur >= prev:
                self.addOne(visited, prev + 1, cur)
            else:
                self.addOne(visited, prev + 1, n)
                self.addOne(visited, 1, cur)
            print(visited)
        maxVisited = max(visited.values())
        for k in visited:
            if visited[k] == maxVisited: ans.append(k)
        return ans

    # simpler solution
    def mostVisited(self, n: int, rounds: list[int]) -> list[int]:
        start, end = rounds[0], rounds[-1]
        if start <= end:
            return list(range(start, end+1))
        return list(range(1, end+1)) + list(range(start, n+1))