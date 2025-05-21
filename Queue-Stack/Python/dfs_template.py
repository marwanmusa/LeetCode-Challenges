from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def dfs(cur: Optional[ListNode], target: Optional[ListNode], visited: set) -> bool:
    if cur is target: return True
    while cur.next:
        if cur.next not in visited:
            visited.add(cur.next)
            if dfs(cur.next, target, visited) == True:
                return True
    return False