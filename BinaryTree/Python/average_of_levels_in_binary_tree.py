from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # using dfs
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        info = []
        def dfs(root, depth = 0):
            if root:
                if len(info) <= depth:
                    info.append([])
                info[depth].append(root.val)
                dfs(root.left, depth+1)
                dfs(root.right, depth+1)
        dfs(root)
        return [sum(x)/len(x) for x in info]
    
    # using stack
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        ans, level = [], [root]
        while root and level:
            cur = [node.val for node in level]
            ans.append(sum(cur)/len(cur))
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ans