from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        c1 = self.get_count(headA)
        c2 = self.get_count(headB)

        if c1 > c2:
            d = c1-c2
            return self.intersect_node(d, headA, headB)
        else:
            d = c2-c1
            return self.intersect_node(d, headB, headA)

    def intersect_node(self, d: int, root1: ListNode, root2: ListNode) -> Optional[ListNode]:
        cur1 = root1
        cur2 = root2
        for i in range(d):
            if cur1 is None:
                return None
            cur1 = cur1.next

        while cur1 != None and cur2 != None:
            if cur1 == cur2:
                return cur1
            cur1 = cur1.next
            cur2 = cur2.next
        return None

    def get_count(self, root: ListNode) -> int:
        count = 0
        cur = root
        while cur.next != None:
            count += 1
            cur = cur.next
        return count