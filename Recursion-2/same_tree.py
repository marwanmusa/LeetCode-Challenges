from collections import deque
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
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.

    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
    """
    # Solution 1
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # Solution 2
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # Solution 3
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
    
    # tupleify
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def t(n):
            return n and (n.val, t(n.left), t(n.right))
        return t(p) == t(q)

    # add iterative solution
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True
        stack = deque([(p, q)])
        while stack:
            p, q = stack.popleft()
            if not check(p, q):
                return False
            if p:
                stack.append((p.right, q.right))
                stack.append((p.left, q.left))
        return True

    
    