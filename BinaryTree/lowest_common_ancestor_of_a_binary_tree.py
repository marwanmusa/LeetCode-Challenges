# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # dfs
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        - Please note that p and q always exist in the tree.
        - Since we dfs from the root down to its children,
          if current root == p or root == q then current root must be their LCA.
        - If left subtree contains one of descendant (p or q) and
          right subtree contains the remaining descendant (q or p) then the root is their LCA.
        - If left subtree contains both p and q then return left as their LCA.
        - If right subtree contains both p and q then return right as their LCA.
        """
        if root in (None, p, q): return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root
        return left or right