class RecentCounter:

    def __init__(self):
        self.que=deque()

    def ping(self, t: int) -> int:
        start=t-3000
        self.que.append(t)
        while(self.que[0]<start):
            self.que.popleft()
        return len(self.que)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)