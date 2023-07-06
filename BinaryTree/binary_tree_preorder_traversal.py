from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursion
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        nodes = []
        if root:
            nodes.append(root.val)
            nodes = nodes + self.preorderTraversal(root.left)
            nodes = nodes + self.preorderTraversal(root.right)
        return nodes

    # dfs
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        def dfs(node):
            if not node:
                return
            # visit root first, then the left subtree, then the right subtree
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res


    # iteration
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = [root]
        while stack:
            currNode = stack.pop()
            if currNode:
                ans.append(currNode.val)
                stack.append(currNode.right)
                stack.append(currNode.left)
        return ans