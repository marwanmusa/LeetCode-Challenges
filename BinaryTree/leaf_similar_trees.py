from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l, r = [], [] 
        def helper(root, ans):
            if root.left: helper(root.left, ans)
            if root and not root.left and not root.right: ans.append(root.val) 
            if root.right: helper(root.right, ans)
        helper(root1, l)
        helper(root2, r)
        return l == r