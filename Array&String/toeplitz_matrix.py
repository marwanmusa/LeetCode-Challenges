class Solution:
    # checking row one by one
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True

    # checking partial matrix
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        return all(r1[:-1] == r2[1:] for r1, r2 in zip(matrix, matrix[1:]))