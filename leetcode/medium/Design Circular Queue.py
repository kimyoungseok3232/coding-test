# https://leetcode.com/problems/design-circular-queue/description/
class MyCircularQueue:

    def __init__(self, k: int):
        self.Cqueue = []
        self.len = k

    def enQueue(self, value: int) -> bool:
        if len(self.Cqueue) < self.len:
            self.Cqueue.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if self.Cqueue:
            self.Cqueue.pop(0)
            return True
        return False

    def Front(self) -> int:
        if self.Cqueue:
            return self.Cqueue[0]
        return -1

    def Rear(self) -> int:
        if self.Cqueue:
            return self.Cqueue[-1]
        return -1

    def isEmpty(self) -> bool:
        return not self.Cqueue

    def isFull(self) -> bool:
        return len(self.Cqueue) == self.len