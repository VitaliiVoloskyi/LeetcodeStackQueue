class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, value):
        node = Node(value)
        if self.last:
            self.last.next = node
        self.last = node
        if self.first is None:
            self.first = node

    def dequeue(self):
        if self.first is None:
            return None
        value = self.first.value
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return value

class MyStack:

    def __init__(self):
        self.main_queue = Queue()
        self.temp_queue = Queue()
        self.last_pushed = None

    def push(self, x: int) -> None:
        self.last_pushed = x
        self.temp_queue.enqueue(x)
        while self.main_queue.first is not None:
            self.temp_queue.enqueue(self.main_queue.dequeue())
        self.main_queue, self.temp_queue = self.temp_queue, self.main_queue

    def pop(self) -> int:
        val = self.main_queue.dequeue()
        if self.main_queue.first is not None:
            self.last_pushed = self.main_queue.first.value
        else:
            self.last_pushed = None
        return val

    def top(self) -> int:
        return self.last_pushed

    def empty(self) -> bool:
        return self.main_queue.first is None


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

