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
