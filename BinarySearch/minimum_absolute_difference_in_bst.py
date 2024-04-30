import bisect
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        els = []
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.left: stack.append(cur.left)
            if cur.right: stack.append(cur.right)
            bisect.insort(els, cur.val)
        minDiff = abs(els[0] - els[1])
        n = len(els)
        if n > 2:
            for i in range(2, len(els)):
                minDiff = min(minDiff, abs(els[i-1]-els[i]))
        return minDiff
    

    # shorter version from above solution
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        store = list()
        def dfs(root):
            if root.left: dfs(root.left)
            store.append(root.val)
            if root.right: dfs(root.right)
        dfs(root)
        return min(b-a for a,b in (zip(store, store[1:])))
