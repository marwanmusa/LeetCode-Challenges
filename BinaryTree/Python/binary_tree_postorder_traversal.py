from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Task:
    Given the root of a binary tree, return the postorder traversal of its nodes' values.
    """
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []
        if root:
            nodes = nodes + self.postorderTraversal(root.left)
            nodes = nodes + self.postorderTraversal(root.right)
            nodes.append(root.val)
        return nodes


    # dfs
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if not node: return
            # visit left subtree first, then the right subtree, and the root
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res


    # iteratively
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    traversal.append(node.val)
                else:
                    # post order
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return traversal

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr:
                stack.append(curr.left)
                stack.append(curr.right)
                res.append(curr.val)
        return res[::-1]


    # Morris traversal
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = deque()
        while root:
            # If there is no right child, go for the left child.
            # Otherwise, find the last node in the right subtree.
            if not root.right:
                res.appendleft(root.val)
                root = root.left
            else:
                last = root.right
                while last.left and last.left != root:
                    last = last.left

                # If the last node is not modified, we let
                # 'root' be its left child. Otherwise, it means we
                # have finished visiting the entire right subtree.
                if not last.left:
                    res.appendleft(root.val)
                    last.left = root
                    root = root.right
                else:
                    last.left = None
                    root = root.left
        return res