from collections import defaultdict
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = []
        stk = [(root, [root.val])]
        while stk:
            cur, path = stk.pop()
            if not cur.left and not cur.right:
                res.append(path)
            if cur.right:
                rpath = path + [cur.right.val]
                stk.append((cur.right, rpath))
            if cur.left:
                lpath = path + [cur.left.val]
                stk.append((cur.left, lpath))
        conv = lambda l: sum(x * 2**i for i, x in enumerate(reversed(l)))
        return sum(map(conv, res))