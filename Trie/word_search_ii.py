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

# Another Solution : Backtracking with Trie

from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None

    def addWord(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        DIR = [0, 1, 0, -1, 0]
        trieNode = TrieNode()
        ans = []
        for word in words:
            trieNode.addWord(word)

        def dfs(r, c, cur):
            if r < 0 or r == m or c < 0 or c == n or board[r][c] not in cur.children: return
            orgChar = board[r][c]
            cur = cur.children[orgChar]
            board[r][c] = '#'  # Mark as visited
            if cur.word != None:
                ans.append(cur.word)
                cur.word = None  # Avoid duplication!
            for i in range(4): dfs(r + DIR[i], c + DIR[i + 1], cur)
            board[r][c] = orgChar  # Restore to org state

        for r in range(m):
            for c in range(n):
                dfs(r, c, trieNode)
        return 
    

# Backtracking II
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = ""
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or len(board) == 0 or not words or len(words) == 0:
            return []
        
        root = TrieNode()
        
        for word in words:
            temp = root
            for letter in word:
                if letter in temp.children:
                    temp = temp.children[letter]
                else:
                    currWord = temp.word
                    temp.children[letter] = TrieNode()
                    temp = temp.children[letter]
                    temp.word = currWord + letter
            temp.isWord = True
        res = []
        
        def backtrack(r, c, node):
            if node.isWord:
                res.append(node.word)
                node.isWord = False
            if r < 0 or r > len(board)-1 or c < 0 or c > len(board[r])-1:
                return
            if board[r][c] not in node.children:
                return
            
            tmpLetter = board[r][c]
            board[r][c] = '$'
            backtrack(r+1, c, node.children[tmpLetter])
            backtrack(r-1, c, node.children[tmpLetter])
            backtrack(r, c+1, node.children[tmpLetter])
            backtrack(r, c-1, node.children[tmpLetter])
            board[r][c] = tmpLetter
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] in root.children:
                    backtrack(r, c, root)
        return res
    

# Another DFS approach
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
        root.end_node = 1

class Solution:
    def findWords(self, board, words):
        self.num_words = len(words)
        res, trie = list(), Trie()
        for word in words: trie.insert(word) 

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.root, i, j, "", res)
        return res

    def dfs(self, board, node, i, j, path, res):
        if self.num_words == 0: return None

        if node.end_node:
            res.append(path)
            node.end_node = False
            self.num_words -= 1

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]): return None
        tmp = board[i][j]
        if tmp not in node.children: return None

        board[i][j] = "#"
        for x,y in [[0,-1], [0,1], [1,0], [-1,0]]:
            self.dfs(board, node.children[tmp], i+x, j+y, path+tmp, res)
        board[i][j] = tmp