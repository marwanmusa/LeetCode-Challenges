import collections
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
    Given the root of a binary tree, return the level order traversal of its nodes' values.
    (i.e., from left to right, level by level).
    """
    # Using stack
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root: return []
        res, q = [], []
        q.append(root)
        while q:
            counter = len(q)
            level_nodes = []
            for i in range(counter):
                node = q[0]
                q.pop(0)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                level_nodes.append(node.val)
            res.append(level_nodes)
        return res

    # Using queue
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root: return []
        res = []
        q = collections.deque([root])
        while q:
            level_nodes = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                level_nodes.append(node.val)
            res.append(level_nodes)
        return res