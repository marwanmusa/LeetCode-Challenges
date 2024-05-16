# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: Node) -> int:
        if not root: return 0
        depth = 0
        for child in root.children:
            depth = max(depth, self.maxDepth(child))
        return depth + 1
    
    # shorter solution
    def maxDepth(self, root: Node) -> int:
        return 1 + max((self.maxDepth(child) for child in root.children), default=0) if root else 0