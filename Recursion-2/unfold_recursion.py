# Unfold recursion means convert a recursion algorithm to non-recursion algorithm.

"""
For example:
 - Determine if two binary trees are the same or not.

Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
"""

from collections import deque

class Solution:
    # Recursive type
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """    
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)
    
    # Non-recursive type
    def isSameTree_non_recursive(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
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