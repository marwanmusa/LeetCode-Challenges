from collections import Counter, defaultdict

class Solution:
    # TLE
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        res, n = 0, len(dominoes)
        for i in range(n-1):
            for j in range(i+1, n):
                if (dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1]) or\
                   (dominoes[i][0] == dominoes[j][1] and dominoes[i][1] == dominoes[j][0]):
                   res += 1
        return res

    # Correct solution
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        count_map = defaultdict(int)
        for a, b in dominoes:
            # Normalize domino pairs
            key = (min(a, b), max(a, b)) # or min(a, b) * 10 + max(a, b)
            count_map[key] += 1

        result = 0
        for count in count_map.values():
            # Add the number of pairs for this domino type
            if count > 1:
                result += count * (count - 1) // 2

        return result

    # one-liner function
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int
        return sum((count * (count - 1) // 2) for count in Counter(tuple(sorted(domino)) for domino in dominoes).values())