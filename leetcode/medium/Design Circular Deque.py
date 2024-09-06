# https://leetcode.com/problems/design-circular-deque/description/

class MyCircularDeque:

    def __init__(self, k: int):
        self.Cdeque = [None] * k
        self.size = k
        self.len = 0
        self.start = 0
        self.last = -1

    def insertFront(self, value: int) -> bool:
        if self.len < self.size:
            self.Cdeque[self.start] = value
            self.start = (self.start+1) % self.size
            self.len += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.len < self.size:
            self.Cdeque[self.last] = value
            self.last = (self.last-1) % self.size
            self.len += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.len > 0:
            self.start = (self.start-1) % self.size
            self.len -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.len > 0:
            self.last = (self.last+1) % self.size
            self.len -= 1
            return True
        return False

    def getFront(self) -> int:
        if self.len > 0:
            return self.Cdeque[(self.start-1)%self.size]
        return -1

    def getRear(self) -> int:
        if self.len > 0:
            return self.Cdeque[(self.last+1)%self.size]
        return -1

    def isEmpty(self) -> bool:
        if self.len > 0:
            return False
        return True

    def isFull(self) -> bool:
        if self.len == self.size:
            return True
        return False