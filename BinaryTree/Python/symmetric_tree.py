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
    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
    """
    # recursively
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        elif self.isMirror(root.left, root.right): return True

    def isMirror(self, A: Optional[TreeNode], B: Optional[TreeNode]) -> bool:
        if A == B == None: return True
        elif A == None or B == None : return False
        return A.val == B.val and self.isMirror(A.left, B.right) and self.isMirror(A.right, B.left)


    # iteratively
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))  # push to the queue
                stack.append((left.right, right.left))
            else:
                return False
        return True