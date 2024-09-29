class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        ans = 0
        def search(board):
            for i in range(8):
                for j in range(8):
                    if board[i][j] == 'R':
                        return [i, j]
        i, j = search(board)
        hl, hr = i - 1, i + 1
        if hl >= 0:
            while hl >= 0:
                if board[hl][j] == 'B' : break
                if board[hl][j] == 'p' :
                    ans += 1
                    break
                hl -= 1

        if hr <= 7:
            while hr <= 7:
                if board[hr][j] == 'B' : break
                elif board[hr][j] == 'p' :
                    ans += 1
                    break
                hr += 1

        vd, vu = j - 1, j + 1
        if vd >= 0:
            while vd >= 0:
                if board[i][vd] == 'B' : break
                elif board[i][vd] == 'p' :
                    ans += 1
                    break
                vd -= 1

        if vu <= 7:
            while vu <= 7:
                if board[i][vu] == 'B' : break
                elif board[i][vu] == 'p' :
                    ans += 1
                    break
                vu += 1
        return ans

