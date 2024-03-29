import collections
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
    Given the root of a binary tree, return the level order traversal of its nodes' values.
    (i.e., from left to right, level by level).

    Example:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

    Input: root = [1]
    Output: [[1]]
    """
    # bfs with stack
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res, q = [], []
        q.append(root)
        while q:
            counter, level_nodes  = len(q), []
            for i in range(counter):
                node = q[0]
                q.pop(0)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                level_nodes.append(node.val)
            res.append(level_nodes)
        return res

    # bfs with queue
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
    
    # A1 another approach
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            lr_pair = [(node.left, node.right) for node in level]
            level = [leaf for LR in lr_pair for leaf in LR if leaf]
        return ans
    
    # A1 shorter
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])            
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ans
    
    # A1 & A2 
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right]) # or temp += [node.left, node.right]
            level = [leaf for leaf in temp if leaf]
        return ans