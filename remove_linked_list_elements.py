from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Task:
    Given the head of a linked list and an integer val,
    remove all the nodes of the linked list that has Node.val == val,
    and return the new head.
    """
    # Method 1
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None: return head
        cur = head
        while cur != None and cur.val == val:
            head = cur.next
            cur = head

        prev = None
        while cur != None:
            while cur!= None and cur.val != val:
                prev = cur
                cur = cur.next

            if cur == None: return head

            prev.next = cur.next
            cur = prev.next

        return head

    # Method 2
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = None
        while head:
            if not temp and head.val != val:
                temp = head
            if head.next and head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return temp
