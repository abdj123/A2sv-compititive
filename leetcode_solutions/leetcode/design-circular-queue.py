class MyCircularQueue:

    def __init__(self, k: int):
        self.Queue=deque()
        self.size=k

    def enQueue(self, value: int) -> bool:
        if len(self.Queue)<self.size:
            self.Queue.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if len(self.Queue)>0:
            self.Queue.popleft()
            return True
        return False

    def Front(self) -> int:
        if self.Queue:
            return self.Queue[0]
        else:
            return -1

    def Rear(self) -> int:
        if self.Queue:
            return self.Queue[-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        return len(self.Queue)==0

    def isFull(self) -> bool:
        return len(self.Queue)==self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()