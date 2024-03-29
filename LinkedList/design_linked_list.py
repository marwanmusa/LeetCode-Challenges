"""
Task:
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node,
and next is a pointer/reference to the next node. If you want to use the doubly linked list,
you will need one more attribute prev to indicate the previous node in the linked list.
Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:
    - MyLinkedList() Initializes the MyLinkedList object.
    - int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
    - void addAtHead(int val) Add a node of value val before the first element of the linked list.
      After the insertion, the new node will be the first node of the linked list.
    - void addAtTail(int val) Append a node of value val as the last element of the linked list.
    - void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list.
      If index equals the length of the linked list, the node will be appended to the end of the linked list.
      If index is greater than the length, the node will not be inserted.
    - void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid
"""

class Node:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        current = self.head

        for _ in range(0, index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be
        the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked
        list, the node will be appended to the end of linked list. If index is greater than the length, the node will not
        be inserted.
        """
        if index > self.size:
            return

        current = self.head
        new_node = Node(val)

        if index <= 0:
            new_node.next = current
            self.head = new_node
        else:
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        current = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0, index - 1):
                current = current.next
            current.next = current.next.next

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


################################################################################
# Doubly Linked-list
class Node():
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        cur = self.head
        while index != 0:
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        self.length += 1
        if self.length == 1:
            self.tail = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        if self.length == 1:
            self.head = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            cur = self.head
            while index-1 != 0:
                cur = cur.next
                index -= 1
            new_node = Node(val)
            new_node.next = cur.next
            cur.next.prev = new_node

            cur.next = new_node
            new_node.prev = cur
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        elif index == 0:
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None
        elif index == self.length-1:
            if self.tail.prev:
                self.tail.prev.next = None
            self.tail = self.tail.prev
            self.length -= 1
            if self.length == 0:
                self.head = None
        else:
            cur = self.head
            while index-1 != 0:
                cur = cur.next
                index -= 1
            cur.next = cur.next.next
            cur.next.prev = cur
            self.length -= 1