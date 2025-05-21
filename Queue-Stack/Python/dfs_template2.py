from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def dfs(root: Optional[ListNode], target: int) -> bool:
    visited = set()
    stack = list()

    stack.append(root)
    while stack:
        cur = stack.pop()
        if cur is target: return True
        while cur.next:
            cur = cur.next
            if cur not in visited:
                visited.add(cur)
                stack.append(cur)
    return False

# Original code in Java
"""
boolean DFS(int root, int target) {
    Set<Node> visited;
    Stack<Node> stack;
    add root to stack;
    while (stack is not empty) {
        Node cur = the top element in stack;
        remove the cur from the stack;
        return true if cur is target;
        for (Node next : the neighbors of cur) {
            if (next is not in visited) {
                add next to visited;
                add next to stack;
            }
        }
    }
    return false;
}
"""