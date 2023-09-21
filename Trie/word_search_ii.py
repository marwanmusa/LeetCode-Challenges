class Solution:
    """
    Task:
    Given an m x n board of characters and a list of strings words, return all words on the board.

    Each word must be constructed from letters of sequentially adjacent cells,
    where adjacent cells are horizontally or vertically neighboring.
    The same letter cell may not be used more than once in a word.
    """
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node[None] = True
        board = {i + 1j*j: c
                 for i, row in enumerate(board) 
                 for j, c in enumerate(row)}
        
        found = []
        def search(node, z, word):
            if node.pop(None, None):
                found.append(word)
            c = board.get(z)
            if c in node:
                board[z] = None
                for k in range(4):
                    search(node[c], z + 1j**k, word+c)
                board[z] = c
        for z in board:
            search(root, z, '')
        return found
    

# Originally by Stefan Pochmann
"""
I first build the tree of words with root `root` and also represent the board a different way,
namely as one-dimensional dictionary where the keys are complex numbers representing the row/column indexes.
That makes further work with it easier. Looping over all board positions is just for z in board,
the four neighbors of a board position z are just z + 1j**k (for k in 0 to 3),
and I don't need to check borders because board.get just returns "None" if I request an invalid position.

After this preparation, I just take the tree and recursively dive with it into each board position.
Similar to how you'd search a single word, but with the tree instead.
"""