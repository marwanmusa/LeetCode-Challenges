from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        Refer to https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/37826/Concise-python-solution-9-lines-space-O(1)

        Level by level traversal with a dummy head prekid.

        root: is for the current level;
        prekid: The dummy head;
        prekid.next: let dummy head's next store the first node of the child level for us;
        kid: is for the child level traversal, to connect each node in child level while moving ahead.

        When this level's work are all done, we move to next level by:
            root = prekid.next   # Just the child level's head
            kid = prekid         # We use this dummy head for the new level's traversal.
            kid.next = None      # Let the dummy head's next be None, before we going for this new level.

        O(1) in Space, O(N) in Time.
        """
        old_root = root
        prekid = Node(0)
        kid = prekid
        while root:
            while root:
                if root.left:
                    kid.next = root.left
                if root.right:
                    kid.next = root.right
                kid = kid.next
                root = root.next
            root, kid = prekid.next, prekid
            kid.next = None
        return old_root