import collections

class Solution:
    def solveSudoku(self, board):
        nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        rows, cols, triples, visit = [collections.defaultdict(set),
                                      collections.defaultdict(set),
                                      collections.defaultdict(set),
                                      collections.deque([])]
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    triples[(r // 3, c // 3)].add(board[r][c])
                else:
                    visit.append((r, c))
        def dfs():
            if not visit:
                return True
            r, c = visit[0]
            t = (r // 3, c // 3)
            for dig in nums:
                if dig not in rows[r] and dig not in cols[c] and dig not in triples[t]:
                    board[r][c] = dig
                    rows[r].add(dig)
                    cols[c].add(dig)
                    triples[t].add(dig)
                    visit.popleft()
                    if dfs():
                        return True
                    else:
                        board[r][c] = "."
                        rows[r].discard(dig)
                        cols[c].discard(dig)
                        triples[t].discard(dig)
                        visit.appendleft((r, c))
            return False
        dfs()


    # another approach
    def solveSudoku(self, board: list[list[str]]) -> None:
        self.board = board
        self.solve()
        
    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row, col
        return -1, -1
        
    def solve(self):
        row, col = self.findUnassigned()
        if (row, col) == (-1, -1):
            return True
                       
        for num in map(str, range(1, 10)):
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = '.'
        
    def isSafe(self, row, col, ch):
        rowSafe = all(self.board[row][_] != ch for _ in range(9))
        colSafe = all(self.board[_][col] != ch for _ in range(9))            
        squareSafe = all(self.board[r][c] != ch for r in self.getRange(row) for c in self.getRange(col))
        return rowSafe and colSafe and squareSafe
    
    def getRange(self, x):
        x -= x % 3
        return range(x, x + 3)
    

    # more clean solution
    def solveSudoku(self, board):
        self.board = board
        self.state = {str(x): 0 for x in range(1, 10)}
        self.initState()
        self.solve()

    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row, col
        return -1, -1
        
    def initState(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] != ".":
                    self.state[self.board[row][col]] += 1

    def isSafe(self, row, col, ch):
        rowSafe = all(self.board[row][_] != ch for _ in range(9))
        colSafe = all(self.board[_][col] != ch for _ in range(9))            
        squareSafe = all(self.board[r][c] != ch for r in self.getRange(row) for c in self.getRange(col))
        return rowSafe and colSafe and squareSafe
    
    def getRange(self, x):
        x -= x % 3
        return range(x, x + 3)
                    
    def solve(self):
        row, col = self.findUnassigned()
        if row == -1 and col == -1:
            return True
               
        for num in set([x for x in self.state if self.state[x] != 9]):
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                self.state[num] += 1
                if self.solve():
                    return True
                self.board[row][col] = "."
                self.state[num] -= 1
        return False