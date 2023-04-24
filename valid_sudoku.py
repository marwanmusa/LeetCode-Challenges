from collections import defaultdict

class Solution:
    """
    Task:
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

    Note:
    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
    """
    # Solution 1 using dict to save temporary row cols and submatrices
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            row, column, block = {}, {}, {}
            row_cube, cols_cube = 3*(i//3), 3*(i%3)
            for j in range(9):
                if board[i][j]!='.' and board[i][j] in row:
                    return False
                row[board[i][j]] = 1
                if board[j][i]!='.' and board[j][i] in column:
                    return False
                column[board[j][i]] = 1
                rc = row_cube+j//3
                cc = cols_cube+j%3
                if board[rc][cc] in block and board[rc][cc]!='.':
                    return False
                block[board[rc][cc]] = 1
        return True

    # Solution 2 using defaultdict to save temporary row cols and submatrices
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows=defaultdict(set)
        cols=defaultdict(set)
        sub_box=defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]=='.':
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in \
                    sub_box[(i//3,j//3)]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                sub_box[(i//3,j//3)].add(board[i][j])
        return True