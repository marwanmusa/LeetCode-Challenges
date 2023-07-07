from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursion
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []
        if root:
            nodes.append(root.val)
            nodes = nodes + self.preorderTraversal(root.left)
            nodes = nodes + self.preorderTraversal(root.right)
        return nodes

    # dfs
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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


    # Morris traversal
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        curr = root
        while curr:
            # If there is no left child, go for the right child.
            # Otherwise, find the last node in the left subtree.
            if not curr.left:
                ans.append(curr.val)
                curr = curr.right
            else:
                last = curr.left
                while last.right and last.right != curr:
                    last = last.right

                # If the last node is not modified, we let
                # 'curr' be its right child. Otherwise, it means we
                # have finished visiting the entire left subtree.
                if not last.right:
                    ans.append(curr.val)
                    last.right = curr
                    curr = curr.left
                else:
                    last.right = None
                    curr = curr.right
        return ans