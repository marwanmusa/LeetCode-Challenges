# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        temp = []
        def helper(root):
            if root.left: helper(root.left)
            if root: temp.append(root.val)
            if root.right: helper(root.right)
        helper(root)
        def build_tree(arr, i, n):
            root = None
            if i < n and arr[i] is not None:
                root = TreeNode(arr[i])
                root.right = build_tree(arr, i+1, n)
            return root
        n = len(temp)
        newnode = build_tree(temp, 0, n)
        return newnode
    
    # another approach
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node, res):
            if node:
                inorder(node.left, res)
                res.append(node.val)
                inorder(node.right, res)
        res = []
        inorder(root, res)
        res = [TreeNode(val=x) for x in res]
        for i in range(len(res)-1):
            res[i].right = res[i+1]
        return res[0]
    
    # modified root only
    def increasingBST(self, root: TreeNode, tail = None) -> TreeNode:
        if not root: return tail
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res
            