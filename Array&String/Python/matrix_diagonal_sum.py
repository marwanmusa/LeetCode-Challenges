class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans, odd = 0, 1 & len(mat)
        mid = len(mat) // 2 if 1 & len(mat) else 0
        for i, sub in enumerate(mat):
            if odd and i == mid:
                ans += sub[i]
            else:
                ans += sub[i] + sub[-(i+1)]
        return ans