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