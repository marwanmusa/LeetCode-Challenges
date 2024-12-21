from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        cur = head
        val, ans = 0, 0
        while cur:
            ans = (val * 2) + cur.val
            val = ans
            cur = cur.next
        return ans