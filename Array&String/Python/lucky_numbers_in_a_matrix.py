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

    # shorter
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        for i, arr in enumerate(matrix):
            min_idx = arr.index(min(arr))
            flag = True
            for j, arr2 in enumerate(matrix):
                if i != j and arr2[min_idx] > arr[min_idx]:
                    flag = False
                    break
            if flag: ans.append(arr[min_idx])
        return ans