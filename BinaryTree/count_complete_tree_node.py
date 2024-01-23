from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  """
  Task:
    Given the root of a complete binary tree, return the number of the nodes in the tree.

    According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
    and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
    
    Design an algorithm that runs in less than O(n) time complexity.
  """
  def countNodes(self, root: Optional[TreeNode]) -> int:
      if not root: return 0
      stack, cnt = [root], 1
      while stack:
          cur = stack.pop()
          if cur.left:
              stack.append(cur.left)
              cnt += 1
          if cur.right:
              stack.append(cur.right)
              cnt += 1
      return cnt
