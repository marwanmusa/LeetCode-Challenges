from threading import Barrier, Lock

# using barrier
class Foo:
    def __init__(self):
        self.first_barrier = Barrier(2)
        self.second_barrier = Barrier(2)

    def first(self, printFirst):
        printFirst()
        self.first_barrier.wait()

    def second(self, printSecond):
        self.first_barrier.wait()
        printSecond()
        self.second_barrier.wait()

    def third(self, printThird):
        self.second_barrier.wait()
        printThird()


# using lock
class Foo:
    def __init__(self):
        self.locks = [Lock(), Lock()]
        self.locks[0].acquire()
        self.locks[1].acquire()

    def first(self, printFirst):
        printFirst()
        self.locks[0].acquire()

    def second(self, printSecond):
        with self.locks[0]:
            printSecond()
            self.locks[1].release()

    def third(self, printThird):
        with self.locks[1]:
            printThird()