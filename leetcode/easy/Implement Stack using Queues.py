# https://leetcode.com/problems/implement-stack-using-queues/description/
from collections import deque
class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.stack.rotate(1)

    def pop(self) -> int:
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return not self.stack