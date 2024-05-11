from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0
        def depth(root):
            l, r = depth(root.left) if root.left else 0, depth(root.right) if root.right else 0
            self.d = max(self.d, l + r)
            return 1 + max(l, r)
        depth(root)
        return self.d
