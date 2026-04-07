class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

class MyQueue:
    def __init__(self):
        self.input_stack = Stack()
        self.output_stack = Stack()

    def push(self, x: int) -> None:
        self.input_stack.push(x)

    def pop(self) -> int:
        if self.output_stack.head is None:
            while self.input_stack.head is not None:
                self.output_stack.push(self.input_stack.pop())
        return self.output_stack.pop()

    def peek(self) -> int:
        if self.output_stack.head is None:
            while self.input_stack.head is not None:
                self.output_stack.push(self.input_stack.pop())
        val = self.output_stack.pop()
        self.output_stack.push(val)
        return val

    def empty(self) -> bool:
        return self.input_stack.head is None and self.output_stack.head is None


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
