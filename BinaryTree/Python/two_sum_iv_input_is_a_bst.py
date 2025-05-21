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
    Given the root of a binary search tree and an integer k,
    return true if there exist two elements in the BST such that
    their sum is equal to k, or false otherwise.
    """
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False

        queue = [root]
        s = set()

        while queue:
            cur = queue.pop()
            val = cur.val
            if (k-val) in s:
                return True
            s.add(val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return False