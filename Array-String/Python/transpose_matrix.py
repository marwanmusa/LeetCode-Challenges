class Solution:
    """
    Task:
        Given a 2D integer array matrix, return the transpose of matrix.
        The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
    """
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]