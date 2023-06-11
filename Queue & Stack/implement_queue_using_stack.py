"""
Task:
    Implement a first in first out (FIFO) queue using only two stacks.
    The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

    Implement the MyQueue class:
        - void push(int x) Pushes element x to the back of the queue.
        - int pop() Removes the element from the front of the queue and returns it.
        - int peek() Returns the element at the front of the queue.
        - boolean empty() Returns true if the queue is empty, false otherwise.

    Notes:
    You must use only standard operations of a stack,
    which means only push to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, the stack may not be supported natively.
    You may simulate a stack using a list or deque (double-ended queue)
    as long as you use only a stack's standard operations.
"""
# Approach 1, push O(1), pop amortized O(1)
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        self.peek()
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        return not self.s1 and not self.s2


# Aproach 2, push O(n), pop O(1)
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while len(self.stack1)>1:
            self.stack2.append(self.stack1.pop())
        self.ans = self.stack1.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return self.ans

    def peek(self) -> int:
        if self.stack1: return self.stack1[0]
        else: return None

    def empty(self) -> bool:
        return True if not self.stack1 else False