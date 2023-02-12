from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        nodes = []
        if root:
            nodes.append(root.val)
            nodes = nodes + self.preorderTraversal(root.left)
            nodes = nodes + self.preorderTraversal(root.right)
        return nodes