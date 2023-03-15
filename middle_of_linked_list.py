from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Task:
    Given the head of a singly linked list, return the middle node of the linked list.

    If there are two middle nodes, return the second middle node.
    """
    # Method 1
    # First we count how many nodes exist n
    # then, return the n//2 node
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = 1
        cur = head
        while cur.next != None:
            cur = cur.next
            c += 1
        for _ in range(c//2):
            head = head.next
        return head

    # Method 2
    # using two pointer
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow