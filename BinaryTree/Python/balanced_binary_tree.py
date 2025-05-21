from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Task:
    Given a binary tree, determine if it is height-balanced.
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # return true if tree is empty
        if root is None:
            return True

        # l & r subtree height
        lh = self.height(root.left)
        rh = self.height(root.right)

        if (abs(lh - rh) <=1) and self.isBalanced(root.left) is True and self.isBalanced(root.right) is True:
            return True

        return False

    def height(self, root: Optional[TreeNode]) -> int:
        # empty tree
        if root is None: return 0

        # non-empty tree
        return 1 + max(self.height(root.left), self.height(root.right))