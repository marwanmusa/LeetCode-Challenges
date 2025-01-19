class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        c = len(matrix[0])
        minr = {i : arr.index(min(arr)) for i, arr in enumerate(matrix)}
        maxc = {}
        for col in range(c):
            mat = [arr[col] for arr in matrix]
            maxc[col] = mat.index(max(mat))
        ans = []
        for k in minr:
            if maxc.get(minr[k]) == k:
                ans.append(matrix[k][minr[k]])
        return ans