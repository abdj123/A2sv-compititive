# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.res = deque()
        self.k = k

    def insertFront(self, value: int) -> bool:
        if len(self.res) < self.k:
            self.res.appendleft(value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.res) < self.k:
            self.res.append(value)
            return True
        return False
        

    def deleteFront(self) -> bool:
        if len(self.res) > 0:
            self.res.popleft()
            return True
        return False

    def deleteLast(self) -> bool:
        if len(self.res) > 0:
            self.res.pop()
            return True
        return False

    def getFront(self) -> int:
        if len(self.res) > 0:
            return self.res[0]
        return -1

    def getRear(self) -> int:
        if len(self.res) > 0:
            return self.res[-1]
        return -1

    def isEmpty(self) -> bool:
        if len(self.res) > 0:
            return False
        return True

    def isFull(self) -> bool:
        if len(self.res) >= self.k:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()