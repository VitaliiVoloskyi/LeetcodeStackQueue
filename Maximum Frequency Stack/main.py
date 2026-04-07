from collections import deque

class FreqStack:

    def __init__(self):
        self.count = {}
        self.stacks_by_freq = {}

    def push(self, val: int) -> None:
        if val in self.count:
            self.count[val] += 1
        else:
            self.count[val] = 1
        freq = self.count[val]
        found = False
        for f in self.stacks_by_freq:
            if f == freq:
                self.stacks_by_freq[f].append(val)
                found = True
                break
        if not found:
            self.stacks_by_freq[freq] = deque([val])

    def pop(self) -> int:
        if not self.stacks_by_freq:
            return None
        max_freq = 0
        for f in self.stacks_by_freq:
            if f > max_freq and self.stacks_by_freq[f]:
                max_freq = f
        val = self.stacks_by_freq[max_freq].pop()
        self.count[val] -= 1

        return val
