from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Task:
    Given the head of a linked list, rotate the list to the right by k places.
    """
    # Excelent method with ll transformation to circular ll
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head:
            return None

        lastElement = head
        length = 1
        # get the length of the list and the last node in the list
        while ( lastElement.next ):
            lastElement = lastElement.next
            length += 1

        # If k is equal to the length of the list then k == 0
        # ElIf k is greater than the length of the list then k = k % length
        k = k % length

        # Set the last node to point to head node
        # The list is now a circular linked list with last node pointing to first node
        lastElement.next = head

        # Traverse the list to get to the node just before the ( length - k )th node.
        # Example: In 1->2->3->4->5, and k = 2
        #          we need to get to the Node(3)
        tempNode = head
        for _ in range( length - k - 1 ):
            tempNode = tempNode.next

        # Get the next node from the tempNode and then set the tempNode.next as None
        # Example: In 1->2->3->4->5, and k = 2
        #          tempNode = Node(3)
        #          answer = Node(3).next => Node(4)
        #          Node(3).next = None ( cut the linked list from here )
        answer = tempNode.next
        tempNode.next = None

        return answer

    # I try to try to traverse all the nodes
    # after it reach k mod len(list)
    # we cut the tail and put it in front of the list
    # but still don't know how to return
    """
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = k % self.length(head)
        cur = head

        if n == 0:
            return head
        else:
            while cur and cur.next:
                if n == 0:
                    tail = cur.next
                    cur.next = None
                    while tail and tail.next:
                        tail = tail.next
                    tail.next = cur
                cur = cur.next
                n -= 1
        # print(tail)
        return cur

    def length(self, head: Optional[ListNode]) -> int:
        n = 1
        cur = head
        while cur and cur.next:
            cur = cur.next
            n += 1
        return n
    """