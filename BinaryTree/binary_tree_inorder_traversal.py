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
    Given the root of a binary tree, return the inorder traversal of its nodes' values.
    """
    # Recursively
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(root, res):
            if root:
                inorder(root.left, res)
                res.append(root.val)
                inorder(root.right, res)
        inorder(root, res)
        return res


    # or simply
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []


    # Iteratively with stack
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []

        # this following "while True" block keeps running until "return"
        while True:
            # goes all the way to left end's None, append every step onto "stack"
            while root:
                stack.append(root)
                root = root.left

            # if stack has nothing left, then return result
            if not stack:
                return res

            # take the last step out, append its value to result
            node = stack.pop()
            res.append(node.val)
            # moves to right before going all the way to left end's None again
            root = node.right


    # another iterative
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                res.append(tmpNode.val)
                root = tmpNode.right
            
        return res


    # Morris Traversal
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = root
        pre = TreeNode()
        while curr:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right:
                    pre = pre.right
                pre.right = curr
                temp = curr
                curr = curr.left
                temp.left = None
        return res
    