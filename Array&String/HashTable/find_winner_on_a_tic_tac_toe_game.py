class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        moveA = [move for i, move in enumerate(moves) if not i & 1]
        moveB = [move for i, move in enumerate(moves) if i & 1]

        def isWin(moves):
            for i in range(3):
                if sum(x[0] == i for x in moves) >= 3 or sum(x[1] == i for x in moves) >= 3: return True
            if ([0, 0] in moves and [1, 1] in moves and [2,2] in moves) or \
               ([0, 2] in moves and [1, 1] in moves and [2,0] in moves): return True
            return False

        if isWin(moveA): return 'A'
        elif isWin(moveB): return 'B'
        elif len(moves) < 9: return 'Pending'
        else: return 'Draw'
