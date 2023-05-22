class MyCircularQueue:
    """
    Task:
    Design your implementation of the circular queue.
    The circular queue is a linear data structure in which the operations are performed
    based on FIFO (First In First Out) principle, and the last position is connected
    back to the first position to make a circle. It is also called "Ring Buffer".

    One of the benefits of the circular queue is that we can make use of the spaces in front of the queue.
    In a normal queue, once the queue becomes full, we cannot insert the next element
    even if there is a space in front of the queue. But using the circular queue,
    we can use the space to store new values.

    Implement the MyCircularQueue class:

    - MyCircularQueue(k) Initializes the object with the size of the queue to be k.
    - int Front() Gets the front item from the queue. If the queue is empty, return -1.
    - int Rear() Gets the last item from the queue. If the queue is empty, return -1.
    - boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
    - boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
    - boolean isEmpty() Checks whether the circular queue is empty or not.
    - boolean isFull() Checks whether the circular queue is full or not.

    You must solve the problem without using the built-in queue data structure in your programming language.
    """
    # Initialize your data structure here. Set the size of the queue to be k.
    def __init__(self, k: int):
        self.data = [None] * k
        self.head = -1
        self.tail = -1
        self.size = k

    # Insert an element into the circular queue. Return true if the operation is successful.
    def enQueue(self, value) -> bool:
        if self.isFull(): return False
        if self.isEmpty(): self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.data[self.tail] = value
        return True

    # Delete an element from the circular queue. Return true if the operation is successful.
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True
        self.head = (self.head + 1) % self.size
        return True

    # Get the last item in front the queue
    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.data[self.head]

    # Get the last item from the queue
    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.data[self.tail]

    # Checks whether the circular queue is empty or not.
    def isEmpty(self) -> bool:
        return self.head == -1

    # Checks whether the circular queue is full or not
    def isFull(self) -> bool:
        return ((self.tail + 1) % self.size) == self.head

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()