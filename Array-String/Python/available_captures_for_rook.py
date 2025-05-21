class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        ans = 0
        def search(board):
            for i in range(8):
                for j in range(8):
                    if board[i][j] == 'R':
                        return [i, j]
        x0, y0 = search(board)
        for i, j in [[1,0], [0,1], [-1,0], [0,-1]]:
            x, y = x0+i, y0+j
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == 'p': ans += 1
                if board[x][y] != '.': break
                x, y = x + i, y + j
        return ans
