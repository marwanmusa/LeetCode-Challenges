from typing import List

class Solution:
    """
    Task:
    In MATLAB, there is a handy function called reshape which can reshape an m x n matrix
    into a new one with a different size r x c keeping its original data.

    You are given an m x n matrix mat and two integers r and c representing the number of rows
    and the number of columns of the wanted reshaped matrix.

    The reshaped matrix should be filled with all the elements of the original matrix
    in the same row-traversing order as they were.

    If the reshape operation with given parameters is possible and legal,
    output the new reshaped matrix; Otherwise, output the original matrix.
    """
    # Using slicing
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flatten, new_mat = [], []
        for row in mat:
            flatten.extend(row)

        if r*c != len(flatten):
            return mat
        else:
            for row_index in range(r):
                new_mat.append(flatten[row_index * c : row_index * c + c])
            return new_mat

    # using assigning
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m*n != r*c:
            return mat

        res = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(m*n):
            row, col = int(i/n), int(i%n)
            new_row, new_col = int(i/c), int(i%c)
            res[new_row][new_col] = mat[row][col]
        return res