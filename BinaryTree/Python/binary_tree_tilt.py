from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root):
            if not root: return 0
            l, r = dfs(root.left), dfs(root.right)
            self.res += abs(l-r)
            return root.val + l + r
        dfs(root)
        return self.res
    

    # storing all tilts in a list and sum all tilts element
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(root, tilts):
            if not root: return 0
            if not root.left and not root.right: return root.val
            l, r = dfs(root.left, tilts), dfs(root.right, tilts)
            tilts.append(abs(l-r))
            return root.val + l + r
        tilts = []
        dfs(root, tilts)
        return sum(tilts)