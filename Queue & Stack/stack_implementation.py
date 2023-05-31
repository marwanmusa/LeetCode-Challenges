class MyStack():
    def __init__(self, data = []):
        self.data = data

    def push(self, x: int) -> None:
        self.data.append(x)

    def isEmpty(self) -> bool:
        return len(self.data) == 0

    def top(self) -> int:
        return self.data[-1]

    def pop(self) -> bool:
        if self.isEmpty():
            return False
        del self.data[-1]
        return True

a = MyStack()
a.push(1)
a.push(2)
a.push(3)
for i in range(4):
    if not a.isEmpty():
        print(a.top())
    print(a.pop())